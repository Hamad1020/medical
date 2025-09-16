import streamlit as st
from PIL import Image

# Custom CSS with medical theme
custom_css = """
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

/* Main theme colors */
:root {
    --primary-blue: #4a90e2; /* Softer blue for a professional look */
    --secondary-blue: #7ab1f2; /* Complementary lighter blue */
    --neutral-gray: #f7f9fc; /* Lighter gray for a cleaner background */
    --dark-gray: #3c3c3c; /* Darker gray for contrast */
    --doctor-white: #ffffff;
    --alert-red: #e74c3c;
    --text-gray: #5a5a5a; /* Soft text color */
}

/* Main container styling */
.main-container {
    max-width: 1000px;
    margin: 0 auto;
    padding: 2rem;
}

/* Header styling */
.medical-header {
    background: var(--neutral-gray);
    padding: 2rem;
    text-align: center;
    margin-bottom: 2rem;
    border-radius: 10px;
    border: 2px solid var(--primary-blue);
}

.medical-header h1 {
    color: var(--primary-blue);
    font-size: 2.2rem;
    font-weight: bold;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* Sidebar styling */
.css-1d391kg {
    background-color: var(--neutral-gray);
    border-right: 2px solid var(--secondary-blue);
    padding: 1.5rem;
}

.css-1d391kg h2 {
    color: var(--primary-blue);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* File uploader styling */
.upload-container {
    border: 2px dashed var(--primary-blue);
    border-radius: 10px;
    padding: 1rem;
    margin: 1rem 0;
    transition: all 0.3s ease;
    text-align: center;
    background-color: rgba(127, 146, 255, 0.05);
}

.upload-container:hover {
    border-color: var(--secondary-blue);
    background-color: rgba(74, 144, 226, 0.1);
}

/* Button styling */
.medical-button {
    background-color: var(--primary-blue);
    color: white;
    border: none;
    padding: 0.75rem 2.5rem;
    border-radius: 25px;
    font-weight: 600;
    transition: all 0.3s ease;
    cursor: pointer;
    margin-top: 1rem;
}

.medical-button:hover {
    background-color: var(--secondary-blue);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

/* Warning card styling */
.warning-card {
    display: flex;
    align-items: center;
    background: var(--neutral-gray);
    border-left: 5px solid var(--alert-red);
    padding: 1rem;
    border-radius: 8px;
    margin-bottom: 1.5rem;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.warning-icon {
    font-size: 2rem;
    color: var(--alert-red);
    margin-right: 0.5rem;
}

.warning-text h4 {
    color: var(--alert-red);
    margin: 0;
}

.warning-text ul {
    margin: 0;
    padding-left: 1.2rem;
    color: var(--dark-gray);
}


/* Card styling for features */
.feature-card {
    background-color: var(--doctor-white);
    border-radius: 10px;
    padding: 1.5rem;
    margin: 1rem 0;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    border-left: 4px solid var(--primary-blue);
}

.feature-card h3 {
    color: var(--primary-blue);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.feature-card p, .feature-card ul {
    color: var(--text-gray);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* Footer */
.footer {
    text-align: center;
    margin-top: 2rem;
    padding: 1rem;
    color: var(--text-gray);
    font-size: 0.8rem;
}

.footer p {
    margin: 0;
}
</style>
"""

# Page configuration
st.set_page_config(
    page_title="Hamad Medical Bot - AI-Powered Medical Assistant",
    page_icon="⚕",
    layout="wide",
)

# Inject custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown('<h2>Hamad Medical Bot ⚕️</h2>', unsafe_allow_html=True)
    st.markdown("### Your AI Medical Assistant")
    st.markdown("---")
    st.markdown("**Features:**")
    st.markdown("• Real-time medical queries")
    st.markdown("• Web-based information access")
    st.markdown("• Latest medical news & treatments")

# Main Content
st.markdown('<div class="medical-header"><h1>Welcome to Hamad Medical Bot ⚕️!</h1></div>', unsafe_allow_html=True)
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown("""
<p style="text-align: center; font-size: 1.2em; color: #666;">
Your intelligent medical assistant powered by AI and real-time web access
</p>
""", unsafe_allow_html=True)

# Features Section
st.markdown("""
<div class="feature-card">
    <h3>🏥 Advanced Medical AI System</h3>
    <ul>
        <li>🔬 <strong>Intelligent Medical Analysis</strong> - Advanced AI-powered medical assistance</li>
        <li>🌐 <strong>Real-time Information Access</strong> - Latest medical research and treatments</li>
        <li>💬 <strong>Natural Conversation</strong> - Human-like medical consultations</li>
        <li>⚡ <strong>24/7 Availability</strong> - Always ready to help with health questions</li>
        <li>🎯 <strong>Personalized Responses</strong> - Tailored medical guidance for your needs</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Caution Section with enhanced warning card
st.markdown("""
<div class="warning-card">
    <div class="warning-icon">⚠</div>
    <div class="warning-text">
        <h4>Important Medical Disclaimer</h4>
        <ul>
            <li>This AI chatbot provides preliminary guidance only and is not a substitute for professional medical advice.</li>
            <li>Always consult qualified healthcare providers for medical conditions.</li>
            <li>In case of emergency, contact your local emergency services immediately.</li>
        </ul>
    </div>
</div>
""", unsafe_allow_html=True)


# Start Conversation Section
st.markdown("""
<div class="feature-card">
    <h3>🩺 Ready to Start Your Medical Consultation?</h3>
    <p>Click below to begin your conversation with Hamad Medical Bot.</p>
</div>
""", unsafe_allow_html=True)

# Main Action Button
st.markdown("---")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🚀 Start Medical Consultation", type="primary", use_container_width=True):
        st.switch_page("pages/Hamad_Medical_Bot.py")

# Feature Description
with st.expander("ℹ️ About Hamad Medical Bot"):
    st.info("""
**Hamad Medical Bot** is your intelligent medical assistant that combines AI technology with real-time web access to provide:

• **Real-time medical queries** - Ask about symptoms, treatments, and health concerns
• **Latest medical information** - Access current medical news and research
• **Web-powered responses** - Get information from reliable medical sources
• **Conversational AI** - Natural, helpful medical conversations

**Important**: This AI provides preliminary guidance only. Always consult healthcare professionals for medical advice.
""")

# Developer Credit Section
st.markdown("---")
st.markdown("""
<div class="feature-card" style="text-align: center; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border-left: none;">
    <h3 style="color: white; margin-bottom: 10px;">👨‍💻 Developed by Hamad Aldohaishi</h3>
    <p style="color: #f0f0f0; margin: 0;">Advanced AI Medical Assistant System</p>
    <p style="color: #e0e0e0; font-size: 0.9em; margin-top: 5px;">Combining cutting-edge artificial intelligence with medical expertise</p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <p>Hamad Medical Bot - Advanced AI Medical Assistant</p>
    <p>Version 1.0.0 | Developed by Hamad Aldohaishi | © 2024 All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
