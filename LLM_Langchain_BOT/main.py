import streamlit as st
from PIL import Image

# Modern Black Theme - Enhanced Human Conversation Design
custom_css = """
<style>
/* Hide Streamlit branding and toolbar */
.viewerBadge_container__1QSob, .viewerBadge_link__1S137, #MainMenu, footer, .stDeployButton,
.stAppToolbar, .stToolbar, .stAppHeader, div[data-testid="stToolbar"], header[data-testid="stHeader"],
button[title="Share"], button[title="Star"], button[title="Edit"], .css-18e3th9 {
    display: none !important;
}

/* Import Modern Fonts */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* Elegant Black Background */
.stApp {
    background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 50%, #0a0a0a 100%);
    color: #ffffff;
    font-family: 'Inter', sans-serif;
    min-height: 100vh;
}

.main .block-container {
    padding-top: 4rem;
    padding-bottom: 4rem;
    max-width: 900px;
    margin: 0 auto;
}

/* Hero Section with Subtle Gradient */
.hero-section {
    text-align: center;
    margin-bottom: 4rem;
    padding: 3rem 2rem;
    position: relative;
}

.hero-section::before {
    content: '';
    position: absolute;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 200px;
    height: 2px;
    background: linear-gradient(90deg, transparent, #00d4ff, transparent);
    border-radius: 1px;
}

.hero-title {
    font-family: 'Inter', sans-serif;
    font-size: 4rem;
    font-weight: 600;
    background: linear-gradient(135deg, #ffffff 0%, #f0f0f0 100%);
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 1.5rem;
    line-height: 1.1;
    letter-spacing: -0.02em;
}

.hero-subtitle {
    font-family: 'Inter', sans-serif;
    font-size: 1.4rem;
    color: #b8b8b8;
    font-weight: 400;
    margin-bottom: 0;
    line-height: 1.5;
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
    opacity: 0.9;
}

/* Elegant Feature Cards */
.feature-card {
    background: linear-gradient(135deg, rgba(255,255,255,0.05) 0%, rgba(255,255,255,0.02) 100%);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 20px;
    padding: 3.5rem 3rem;
    margin: 3rem 0;
    backdrop-filter: blur(10px);
    position: relative;
    overflow: hidden;
}

.feature-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(0,212,255,0.3), transparent);
}

.feature-icon {
    font-size: 2.8rem;
    margin-bottom: 1.5rem;
    display: block;
    background: linear-gradient(135deg, #00d4ff, #00ff88);
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.feature-title {
    font-family: 'Inter', sans-serif;
    font-size: 1.6rem;
    font-weight: 600;
    color: #ffffff;
    margin-bottom: 2rem;
    letter-spacing: -0.01em;
}

.feature-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

.feature-list li {
    font-family: 'Inter', sans-serif;
    color: #d4d4d4;
    margin-bottom: 1.2rem;
    line-height: 1.7;
    font-size: 1.05rem;
    opacity: 0.9;
}

.feature-list li::before {
    content: '▸';
    color: #00d4ff;
    font-weight: bold;
    margin-right: 0.75rem;
    font-size: 1.1rem;
}

/* Warning Card with Subtle Red Tint */
.warning-card {
    background: linear-gradient(135deg, rgba(220,38,38,0.05) 0%, rgba(220,38,38,0.02) 100%);
    border: 1px solid rgba(220,38,38,0.2);
    border-radius: 20px;
    padding: 3rem 3rem;
    margin: 4rem 0;
    backdrop-filter: blur(10px);
}

.warning-content {
    display: flex;
    align-items: flex-start;
    gap: 1.5rem;
}

.warning-icon {
    font-size: 2.2rem;
    color: #ff6b35;
    margin-top: 0.25rem;
    filter: drop-shadow(0 0 8px rgba(255,107,53,0.3));
}

.warning-text {
    flex: 1;
}

.warning-title {
    font-family: 'Inter', sans-serif;
    font-size: 1.3rem;
    font-weight: 600;
    color: #ff6b35;
    margin: 0 0 1.5rem 0;
}

.warning-list {
    font-family: 'Inter', sans-serif;
    color: #e5e5e5;
    margin: 0;
    padding-left: 0;
    line-height: 1.7;
}

.warning-list li {
    margin-bottom: 1rem;
    list-style: none;
}

/* Dark Modern Button Styling */
.stButton > button {
    background: linear-gradient(135deg, #1e1b4b 0%, #312e81 100%) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 14px !important;
    padding: 1.2rem 3rem !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    font-size: 1.1rem !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    box-shadow: 0 4px 15px rgba(30,27,75,0.4) !important;
    position: relative !important;
    overflow: hidden !important;
}

.stButton > button::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.15), transparent);
    transition: left 0.6s;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #0f0a19 0%, #1e1b4b 100%) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 25px rgba(30,27,75,0.6) !important;
}

.stButton > button:hover::before {
    left: 100%;
}

/* Elegant Developer Credit */
.developer-credit {
    background: linear-gradient(135deg, rgba(255,255,255,0.03) 0%, rgba(255,255,255,0.01) 100%);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 20px;
    padding: 3.5rem 3rem;
    text-align: center;
    margin: 5rem 0;
    backdrop-filter: blur(10px);
    position: relative;
}

.developer-credit::before {
    content: '';
    position: absolute;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 100px;
    height: 1px;
    background: linear-gradient(90deg, transparent, #00ff88, transparent);
}

.developer-title {
    font-family: 'Inter', sans-serif;
    font-size: 1.6rem;
    font-weight: 600;
    margin-bottom: 0.75rem;
    color: #ffffff;
}

.developer-subtitle {
    font-family: 'Inter', sans-serif;
    color: #b8b8b8;
    margin: 0;
    font-size: 1.1rem;
    opacity: 0.8;
}

/* Enhanced Responsive Design */
@media (max-width: 768px) {
    .hero-title {
        font-size: 3rem;
    }

    .hero-subtitle {
        font-size: 1.2rem;
    }

    .feature-card {
        padding: 2.5rem 2rem;
        margin: 2.5rem 0;
    }

    .warning-card {
        padding: 2.5rem 2rem;
    }

    .developer-credit {
        padding: 2.5rem 2rem;
        margin: 4rem 0;
    }

    .stButton > button {
        padding: 1rem 2.5rem !important;
        font-size: 1rem !important;
    }

    .warning-content {
        flex-direction: column;
        gap: 1rem;
    }

    .warning-icon {
        align-self: center;
        margin-top: 0;
    }
}

@media (max-width: 480px) {
    .hero-title {
        font-size: 2.2rem;
    }

    .hero-subtitle {
        font-size: 1.1rem;
    }

    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    .feature-card,
    .warning-card,
    .developer-credit {
        padding: 2rem 1.5rem;
    }
}

/* Smooth Animations */
.stApp {
    animation: fadeIn 1s ease-out;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(15px); }
    to { opacity: 1; transform: translateY(0); }
}
</style>
"""

# Page configuration
st.set_page_config(
    page_title="Hamad Medical Bot - Your Human-like Health Conversation Partner",
    page_icon="💬",
    layout="wide",
)

# Inject custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Enhanced Hero Section
st.markdown("""
<div class="hero-section">
    <h1 class="hero-title">Hamad Medical Bot</h1>
    <p class="hero-subtitle">Your intelligent health companion that understands you like a trusted friend</p>
</div>
""", unsafe_allow_html=True)

# Enhanced Human-like Conversation Features
st.markdown("""
<div class="feature-card">
    <span class="feature-icon">💬</span>
    <h3 class="feature-title">Your Personal Health Conversation Partner</h3>
    <ul class="feature-list">
        <li><strong>Authentic Conversations:</strong> Engage in natural, flowing dialogue about your health just like speaking with a caring healthcare professional</li>
        <li><strong>Intelligent Memory:</strong> Remembers your entire conversation history to provide deeply personalized and contextually relevant advice</li>
        <li><strong>Emotional Intelligence:</strong> Responds with genuine empathy and understanding, recognizing when you need support beyond just facts</li>
        <li><strong>Crystal Clear Communication:</strong> Transforms complex medical terminology into simple, accessible language you can easily understand</li>
        <li><strong>Active Listening:</strong> Asks thoughtful follow-up questions to fully comprehend your unique situation and concerns</li>
        <li><strong>Compassionate Care:</strong> Combines medical knowledge with genuine care, always prioritizing your well-being and safety</li>
        <li><strong>24/7 Emotional Support:</strong> Available whenever you need someone to talk to about your health worries, day or night</li>
        <li><strong>Holistic Understanding:</strong> Considers both your physical symptoms and emotional well-being in every conversation</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Enhanced Warning Section
st.markdown("""
<div class="warning-card">
    <div class="warning-content">
        <div class="warning-icon">🤝</div>
        <div class="warning-text">
            <h4 class="warning-title">Your Health Journey Partner</h4>
            <ul class="warning-list">
                <li>I'm your caring conversation partner for health discussions, but I'm not a substitute for professional medical advice or treatment</li>
                <li>For serious symptoms, emergencies, or complex health conditions, please consult licensed healthcare professionals</li>
                <li>If you're experiencing a medical emergency, call emergency services immediately - I'm here to support, not replace, professional care</li>
                <li>Think of me as your knowledgeable friend who can help you prepare for and understand your healthcare conversations</li>
            </ul>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Conversational About Section
st.markdown("""
<div class="feature-card">
    <span class="feature-icon">🤝</span>
    <h3 class="feature-title">About Our Conversation</h3>
    <p style="font-family: 'Inter', sans-serif; color: #d4d4d4; line-height: 1.7; margin-bottom: 1.5rem; font-size: 1.05rem;">
    Hamad Medical Bot represents a new era of healthcare communication - where advanced AI meets genuine human connection. Built with cutting-edge conversational AI, I combine medical knowledge with emotional intelligence to create truly meaningful health discussions.
    </p>
    <p style="font-family: 'Inter', sans-serif; color: #d4d4d4; line-height: 1.7; margin-bottom: 1.5rem; font-size: 1.05rem;">
    Whether you're researching symptoms, seeking clarification on medical terms, preparing for a doctor's appointment, or simply need someone compassionate to talk to about your health worries - I'm here. My responses are crafted to be both medically accurate and emotionally supportive, helping you feel heard, understood, and empowered in your health journey.
    </p>
    <p style="font-family: 'Inter', sans-serif; color: #b8b8b8; line-height: 1.6; margin: 0; font-style: italic; opacity: 0.9;">
    "Where technology meets compassion in healthcare conversations."
    </p>
</div>
""", unsafe_allow_html=True)

# Enhanced Action Button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("💬 Start Your Health Conversation", type="primary", use_container_width=True):
        st.switch_page("pages/Hamad_Medical_Bot.py")

# Enhanced Developer Credit
st.markdown("""
<div class="developer-credit">
    <h3 class="developer-title">Crafted with ❤️ by Hamad Aldohaishi</h3>
    <p class="developer-subtitle">Bringing human warmth to AI healthcare conversations</p>
</div>
""", unsafe_allow_html=True)
