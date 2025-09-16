# Hamad Medical Bot

A streamlined AI-powered medical assistant that provides preliminary medical guidance using GPT-4o and real-time web access.

## Features

- **Medical Q&A**: Ask medical questions and get AI-powered responses
- **Web Access**: Real-time information retrieval for current medical data
- **Conversational AI**: Maintains conversation history for contextual responses
- **Medical Focus**: Specialized for healthcare-related queries

## Setup

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

- **Frontend**: Streamlit web interface
- **AI Model**: GPT-4o via OpenAI API
- **Web Search**: DuckDuckGo integration
- **Memory**: Conversation history management

## License

All rights reserved - Hamad Medical Bot © 2024