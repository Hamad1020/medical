import utils
import streamlit as st

from langchain import hub
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.callbacks import StreamlitCallbackHandler
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.tools import Tool
from langchain_community.chat_message_histories import ChatMessageHistory

st.header('Hamad Medical Bot - AI Medical Assistant')
st.write('Your intelligent medical assistant powered by AI and real-time web access')
st.caption("Ask medical questions and get responses based on the latest web information")
st.caption("⚠️ This AI provides preliminary guidance only. Always consult healthcare professionals for medical advice.")
class InternetChatbot:

    def __init__(self):
        utils.sync_st_session()
        self.llm = utils.configure_llm()

    # @st.cache_resource(show_spinner='Connecting..')
    def setup_agent(_self):
        # Define tool
        ddg_search = DuckDuckGoSearchRun()
        tools = [
            Tool(
                name="DuckDuckGoSearch",
                func=ddg_search.run,
                description="Useful for when you need to answer questions about current events. You should ask targeted questions",
            )
        ]

        # Get the prompt and customize it for medical queries
        prompt = hub.pull("hwchase17/react-chat")
        # Add medical context to the system message
        if hasattr(prompt, 'template'):
            prompt.template = prompt.template.replace(
                "You are a helpful assistant",
                "You are Hamad Medical Bot, a helpful medical assistant. Focus on medical questions and use web search when needed for current information. Always remind users that you're not a substitute for professional medical advice."
            )

        # Setup LLM and Agent
        memory = ConversationBufferMemory(memory_key="chat_history")
        agent = create_react_agent(_self.llm, tools, prompt)
        agent_executor = AgentExecutor(
            agent=agent,
            tools=tools,
            memory=memory,
            verbose=False,
            handle_parsing_errors=True,
            max_iterations=3,  # Limit iterations to prevent infinite loops
            max_execution_time=30,  # 30 second timeout
        )
        return agent_executor, memory

    @utils.enable_chat_history
    def main(self):
        agent_executor, memory = self.setup_agent()
        user_query = st.chat_input(placeholder="Ask me anything!")
        try:
            if user_query:
                utils.display_msg(user_query, 'user')
                with st.chat_message("assistant"):
                    st_cb = StreamlitCallbackHandler(st.container())
                    # Get chat history from session state instead of memory object
                    chat_history = []
                    if "messages" in st.session_state:
                        # Convert messages to the format expected by the agent
                        for msg in st.session_state.messages[-10:]:  # Last 10 messages to avoid context being too long
                            if msg["role"] == "user":
                                chat_history.append(f"Human: {msg['content']}")
                            elif msg["role"] == "assistant":
                                chat_history.append(f"Assistant: {msg['content']}")

                    result = agent_executor.invoke(
                        {"input": user_query, "chat_history": chat_history},
                        {"callbacks": [st_cb]}
                    )
                    response = result["output"]
                    st.session_state.messages.append({"role": "assistant", "content": response})
                    st.write(response)
                    utils.print_qa(InternetChatbot, user_query, response)
        except Exception as e:
            error_msg = str(e)
            print(f"Agent error: {error_msg}")

            # Try fallback: direct LLM call without agent
            try:
                fallback_prompt = f"""You are Hamad Medical Bot, a helpful medical assistant. Answer this medical question based on general knowledge. Always remind the user that you're not a substitute for professional medical advice.

Question: {user_query}

Answer:"""

                with st.spinner("Getting response..."):
                    fallback_response = self.llm.invoke(fallback_prompt).content

                st.success("✅ Response generated using fallback method:")
                st.write(fallback_response)
                st.session_state.messages.append({"role": "assistant", "content": fallback_response})
                utils.print_qa(InternetChatbot, user_query, fallback_response)

            except Exception as fallback_error:
                print(f"Fallback error: {fallback_error}")

                # Final error handling
                if "rate limit" in error_msg.lower():
                    st.error("⚠️ Rate limit exceeded. Please wait a moment and try again.")
                elif "timeout" in error_msg.lower() or "max_execution_time" in error_msg.lower():
                    st.error("⚠️ Request timed out. Please try a simpler question.")
                elif "too many requests" in error_msg.lower():
                    st.error("⚠️ Too many requests. Please wait a moment and try again.")
                else:
                    st.warning("Some error occurred while processing your request. Please try a simpler or different question.")

                utils.print_qa(InternetChatbot, user_query, f"Error: {error_msg}")
                

if __name__ == "__main__":
    try:
        obj = InternetChatbot()
        obj.main()
    except Exception as e:
        st.warning("Section Under Maintenance,Comeback Later!Check our Prescription decoder section until that!")
        st.info(f"Error details: {e}")
