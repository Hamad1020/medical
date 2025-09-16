import json
import os
import sys

# Set up environment
os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY", "")

# Import required modules
import openai
from openai import OpenAI

# Global conversation history storage
conversation_history = {}

def handler(event, context):
    """Netlify function to handle chat requests - simplified for testing"""

    # Set CORS headers
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Content-Type': 'application/json'
    }

    # Handle preflight requests
    if event.get('httpMethod') == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': headers,
            'body': ''
        }

    if event.get('httpMethod') != 'POST':
        return {
            'statusCode': 405,
            'headers': headers,
            'body': json.dumps({'error': 'Method not allowed'})
        }

    try:
        # Parse request body safely
        try:
            body = json.loads(event.get('body', '{}'))
        except:
            body = {}

        user_message = body.get('message', '').strip()
        session_id = body.get('session_id', 'default')

        if not user_message:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({'error': 'No message provided'})
            }

        # Simple response for now - test if function works
        if 'hello' in user_message.lower() or 'hi' in user_message.lower():
            response = "Hello! I'm Hamad Medical Bot, your AI medical assistant. How can I help you with health-related questions today?"
        elif 'pain' in user_message.lower():
            response = "I understand you're experiencing pain. While I can provide general information, please consult a healthcare professional for proper diagnosis and treatment. Can you describe the type and location of your pain?"
        else:
            response = f"Thank you for your question about '{user_message}'. I'm here to help with medical questions. For personalized medical advice, please consult a qualified healthcare professional. What specific health concern would you like information about?"

        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({
                'response': response,
                'session_id': session_id
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({
                'error': f'Error: {str(e)}'
            })
        }
