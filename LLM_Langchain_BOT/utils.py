import os
import streamlit as st
from datetime import datetime
from streamlit.logger import get_logger
import openai

logger = get_logger('Langchain-Chatbot')

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

#decorator
def enable_chat_history(func):
    # Always enable chat history since we have a fixed API key

    # to clear chat history after switching chatbot
    current_page = func.__qualname__
    if "current_page" not in st.session_state:
        st.session_state["current_page"] = current_page
    if st.session_state["current_page"] != current_page:
        try:
            st.cache_resource.clear()
            del st.session_state["current_page"]
            del st.session_state["messages"]
        except:
            pass

    # to show chat history on ui
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I solve your medical queries?"}]
    for msg in st.session_state["messages"]:
        st.chat_message(msg["role"]).write(msg["content"])

    def execute(*args, **kwargs):
        func(*args, **kwargs)
    return execute

def display_msg(msg, author):
    """Method to display message on the UI

    Args:
        msg (str): message to display
        author (str): author of the message -user/assistant
    """
    st.session_state.messages.append({"role": author, "content": msg})
    st.chat_message(author).write(msg)

def choose_custom_openai_key():
    openai_api_key = st.sidebar.text_input(
        label="OpenAI API Key",
        type="password",
        placeholder="sk-...",
        key="SELECTED_OPENAI_API_KEY"
        )
    if not openai_api_key:
        st.error("Please add your OpenAI API key to continue.")
        st.info("Obtain your key from this link: https://platform.openai.com/account/api-keys")
        st.stop()

    model = "gpt-4o"
    try:
        # Completely remove proxy environment variables
        proxy_env_vars = ['HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy', 'ALL_PROXY', 'no_proxy', 'NO_PROXY']
        for var in proxy_env_vars:
            if var in os.environ:
                del os.environ[var]

        client = openai.OpenAI(api_key=openai_api_key)
        available_models = [{"id": i.id, "created":datetime.fromtimestamp(i.created)} for i in client.models.list() if str(i.id).startswith("gpt")]
        available_models = sorted(available_models, key=lambda x: x["created"])
        available_models = [i["id"] for i in available_models]

        model = st.sidebar.selectbox(
            label="Model",
            options=available_models,
            key="SELECTED_OPENAI_MODEL"
        )
    except openai.AuthenticationError as e:
        st.error(e.body["message"])
        st.stop()
    except Exception as e:
        print(e)
        st.error("Something went wrong. Please try again later.")
        st.stop()
    return model, openai_api_key

def configure_llm():
    # Set API key as environment variable first
    api_key = "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"
    
    # Set as environment variable
    os.environ["OPENAI_API_KEY"] = api_key.strip()

    # Completely remove proxy environment variables
    proxy_env_vars = ['HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy', 'ALL_PROXY', 'no_proxy', 'NO_PROXY']
    for var in proxy_env_vars:
        if var in os.environ:
            del os.environ[var]

    # Return OpenAI client using environment variable
    return openai.OpenAI()

def print_qa(cls, question, answer):
    log_str = "\nUsecase: {}\nQuestion: {}\nAnswer: {}\n" + "------"*10
    logger.info(log_str.format(cls.__name__, question, answer))

@st.cache_resource
def configure_embedding_model():
    embedding_model = FastEmbedEmbeddings(model_name="BAAI/bge-small-en-v1.5")
    return embedding_model

def sync_st_session():
    for k, v in st.session_state.items():
        st.session_state[k] = v
        
def get_prompt_template():
    template = f"""You are an AI-powered Virtual Health Assistant designed to provide preliminary consultations and answer health-related queries for patients in remote areas. Use the chat history and the user's question to provide a helpful, accurate, and empathetic response. If the query involves a medical emergency, always advise the user to seek immediate professional medical help."""
    return template
# Chat History:
# {chat_history}"""
