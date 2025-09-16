# Hamad Medical Bot

A streamlined AI-powered medical assistant that provides preliminary medical guidance using GPT-4o and real-time web access.

## Features

- **Medical Q&A**: Ask medical questions and get AI-powered responses
- **Web Access**: Real-time information retrieval for current medical data
- **Conversational AI**: Maintains conversation history for contextual responses
- **Medical Focus**: Specialized for healthcare-related queries

## Deployment Options

### Option 1: Streamlit Cloud (Recommended)

1. Go to [Streamlit Cloud](https://share.streamlit.io/)
2. Connect your GitHub repository: `https://github.com/Hamad1020/medical.git`
3. Set main file path: `LLM_Langchain_BOT/main.py`
4. Add environment variable: `OPENAI_API_KEY=your_api_key_here`
5. Deploy

### Option 2: Netlify (Alternative)

1. **Connect Repository**: Link your GitHub repo to Netlify
2. **Build Settings**:
   - Build command: (leave empty)
   - Publish directory: `build` (but this will be overridden)
3. **Environment Variables**:
   - `OPENAI_API_KEY`: Your OpenAI API key
4. **Deploy**

## Local Development

1. Clone the repository:
```bash
git clone https://github.com/Hamad1020/medical.git
cd medical
```

2. Install dependencies:
```bash
pip install -r LLM_Langchain_BOT/requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

4. Run the application:
```bash
cd LLM_Langchain_BOT
streamlit run main.py
```

## Environment Variables

Create a `.env` file with:
```
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

1. Open the application in your browser
2. Click "Start Medical Consultation"
3. Ask medical questions in natural language
4. The AI will provide responses based on medical knowledge and web search

## Important Disclaimer

⚠️ **This AI provides preliminary guidance only and is not a substitute for professional medical advice. Always consult qualified healthcare providers for medical conditions.**

## Architecture

### Streamlit Cloud Version
- **Frontend**: Streamlit web interface
- **AI Model**: GPT-4o via OpenAI API
- **Web Search**: DuckDuckGo integration
- **Memory**: Conversation history management

### Netlify Version
- **Frontend**: Vanilla HTML/JavaScript
- **Backend**: Netlify Functions (Python)
- **AI Model**: GPT-4o via OpenAI API
- **Web Search**: DuckDuckGo integration
- **Memory**: Session-based conversation history

## License

All rights reserved - Hamad Medical Bot © 2024