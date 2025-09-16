import json
import os
import sys
from pathlib import Path

# Add the LLM_Langchain_BOT directory to Python path
sys.path.append(str(Path(__file__).parent.parent.parent / "LLM_Langchain_BOT"))

import utils
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory

def handler(event, context):
    """Netlify function to handle chat requests"""

    # Set CORS headers
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Content-Type': 'application/json'
    }

    # Handle preflight requests
    if event['httpMethod'] == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': headers,
            'body': ''
        }

    if event['httpMethod'] != 'POST':
        return {
            'statusCode': 405,
            'headers': headers,
            'body': json.dumps({'error': 'Method not allowed'})
        }

    try:
        # Parse request body
        body = json.loads(event['body'])
        user_message = body.get('message', '')
        session_id = body.get('session_id', 'default')

        if not user_message:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({'error': 'No message provided'})
            }

        # Initialize LLM
        llm = utils.configure_llm()

        # Create prompt template
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are Hamad Medical Bot, a helpful medical assistant. Answer medical questions based on general knowledge. Always remind users that you're not a substitute for professional medical advice."),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}")
        ])

        # Create chain
        chain = prompt | llm

        # Session management
        sessions = {}

        def get_session_history(session_id_param):
            if session_id_param not in sessions:
                sessions[session_id_param] = ChatMessageHistory()
            return sessions[session_id_param]

        conversation_chain = RunnableWithMessageHistory(
            runnable=chain,
            get_session_history=get_session_history,
            input_messages_key="input",
            history_messages_key="history"
        )

        # Get response
        result = conversation_chain.invoke(
            {"input": user_message},
            config={"configurable": {"session_id": session_id}}
        )

        response = result.content

        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({
                'response': response,
                'session_id': session_id
            })
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({
                'error': 'Internal server error',
                'details': str(e)
            })
        }
