import utils
import streamlit as st
from streaming import StreamHandler

# Hide GitHub and Streamlit branding
st.markdown("""
<style>
/* Hide GitHub link and Streamlit branding */
.viewerBadge_container__1QSob {
    display: none !important;
}

.viewerBadge_link__1S137 {
    display: none !important;
}

/* Hide any GitHub-related elements */
a[href*="github"] {
    display: none !important;
}

/* Hide Streamlit menu and footer */
#MainMenu {
    display: none !important;
}

footer {
    display: none !important;
}

.stDeployButton {
    display: none !important;
}

/* Hide top-right toolbar with GitHub and edit buttons */
.stAppToolbar {
    display: none !important;
}

.stToolbar {
    display: none !important;
}

/* Hide the entire top toolbar area */
.stAppHeader {
    display: none !important;
}

/* Hide share, star, and edit buttons */
button[title="Share"] {
    display: none !important;
}

button[title="Star"] {
    display: none !important;
}

button[title="Edit"] {
    display: none !important;
}

/* Hide toolbar container */
div[data-testid="stToolbar"] {
    display: none !important;
}

/* Hide the entire header area */
header[data-testid="stHeader"] {
    display: none !important;
}

/* Additional specific targeting for toolbar elements */
.css-18e3th9 {
    display: none !important;
}

.css-1d391kg .css-18e3th9 {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

st.header('Hamad Medical Bot - AI Medical Assistant')
st.write('Your intelligent medical assistant powered by AI')
st.caption("Ask medical questions and get AI-powered responses")
st.caption("⚠️ This AI provides preliminary guidance only. Always consult healthcare professionals for medical advice.")

# Global conversation history storage
conversation_history = {}

@utils.enable_chat_history
def main():
    # Initialize OpenAI client
    client = utils.configure_llm()
    
    user_query = st.chat_input(placeholder="Ask me about your health concerns...")
    if user_query:
        utils.display_msg(user_query, 'user')
        
        with st.chat_message("assistant"):
            st_cb = StreamHandler(st.empty())
            
            try:
                # Get conversation history for this session
                session_id = "default_session"
                if session_id not in conversation_history:
                    conversation_history[session_id] = []
                
                # Prepare messages for OpenAI
                messages = [
                    {
                        "role": "system",
                        "content": "You are Hamad Medical Bot, an advanced AI medical assistant developed by Hamad Aldohaishi (حمد الدهيشي ولد عبدالله). You are a sophisticated medical AI system designed to provide accurate, helpful medical information based on established medical knowledge. Always be empathetic, clear, and professional. Include relevant disclaimers when appropriate, but don't over-warn users unnecessarily. Focus on being genuinely helpful while maintaining medical accuracy. If anyone asks about your development or who created you, mention that you were developed by Hamad Aldohaishi (حمد الدهيشي ولد عبدالله). Do not mention specific AI model names - simply refer to yourself as an advanced AI medical system."
                    }
                ]
                
                # Add conversation history (limit to last 10 messages to avoid token limits)
                for msg in conversation_history[session_id][-10:]:
                    messages.append(msg)
                
                # Add current user message
                messages.append({
                    "role": "user",
                    "content": user_query
                })
                
                # Get response from GPT-4o
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=messages,
                    max_tokens=1000,
                    temperature=0.7,
                    stream=True
                )
                
                # Stream the response
                full_response = ""
                for chunk in response:
                    if chunk.choices[0].delta.content:
                        content = chunk.choices[0].delta.content
                        full_response += content
                        st_cb.on_llm_new_token(content)
                
                # Store conversation in history
                conversation_history[session_id].append({
                    "role": "user",
                    "content": user_query
                })
                conversation_history[session_id].append({
                    "role": "assistant", 
                    "content": full_response
                })
                
                # Limit history to prevent memory issues
                if len(conversation_history[session_id]) > 20:  # Keep last 10 exchanges
                    conversation_history[session_id] = conversation_history[session_id][-20:]
                
                st.session_state.messages.append({"role": "assistant", "content": full_response})
                utils.print_qa(main, user_query, full_response)
                
            except Exception as e:
                error_msg = str(e)
                print(f"Error: {error_msg}")
                
                # Show the actual error for debugging
                with st.expander("🔍 Debug Info (Click to expand)"):
                    st.code(f"Full error: {error_msg}")
                    st.code(f"API Key (last 10 chars): ...{client.api_key[-10:] if hasattr(client, 'api_key') else 'No key found'}")
                
                if "rate limit" in error_msg.lower():
                    st.error("⚠️ Rate limit exceeded. Please wait a moment and try again.")
                elif "timeout" in error_msg.lower():
                    st.error("⚠️ Request timed out. Please try again.")
                elif "too many requests" in error_msg.lower():
                    st.error("⚠️ Too many requests. Please wait a moment and try again.")
                elif "invalid_api_key" in error_msg.lower() or "401" in error_msg:
                    st.error("⚠️ API key issue detected. Please check your OpenAI API key.")
                elif "model" in error_msg.lower() and "does not exist" in error_msg.lower():
                    st.error("⚠️ Model access issue. GPT-4o might not be available for your API key.")
                else:
                    st.error("Some error occurred. Please try again.")
                
                utils.print_qa(main, user_query, f"Error: {error_msg}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        st.error(f"Application error: {e}")
