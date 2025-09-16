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
    """Netlify function to handle chat requests"""
    print(f"DEBUG: Function called with method: {event.get('httpMethod', 'UNKNOWN')}")

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
        body = json.loads(event.get('body', '{}'))
        user_message = body.get('message', '').strip()
        session_id = body.get('session_id', 'default')

        if not user_message:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({'error': 'No message provided'})
            }

        # Check for OpenAI API key
        api_key = os.environ.get('OPENAI_API_KEY', '')
        print(f"DEBUG: API key present: {bool(api_key)}")
        if not api_key:
            print("DEBUG: No OpenAI API key found")
            return {
                'statusCode': 500,
                'headers': headers,
                'body': json.dumps({'error': 'OpenAI API key not configured. Please check your Netlify environment variables.'})
            }

        # Initialize OpenAI client
        client = OpenAI(api_key=api_key)

        # Get conversation history for this session
        if session_id not in conversation_history:
            conversation_history[session_id] = []

        # Prepare messages for OpenAI
        messages = [
            {
                "role": "system",
                "content": "You are Hamad Medical Bot, a helpful and knowledgeable medical assistant. Provide accurate, helpful medical information based on established medical knowledge. Always be empathetic, clear, and professional. Include relevant disclaimers when appropriate, but don't over-warn users unnecessarily. Focus on being genuinely helpful while maintaining medical accuracy."
            }
        ]

        # Add conversation history (limit to last 10 messages to avoid token limits)
        for msg in conversation_history[session_id][-10:]:
            messages.append(msg)

        # Add current user message
        messages.append({
            "role": "user",
            "content": user_message
        })

        # Get response from GPT-4o
        print(f"DEBUG: Making OpenAI API call with {len(messages)} messages")
        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                max_tokens=1000,
                temperature=0.7
            )
            ai_response = response.choices[0].message.content
            print(f"DEBUG: Got response from OpenAI: {len(ai_response)} characters")
        except Exception as api_error:
            print(f"DEBUG: OpenAI API error: {str(api_error)}")
            return {
                'statusCode': 500,
                'headers': headers,
                'body': json.dumps({'error': f'OpenAI API error: {str(api_error)}'})
            }

        # Store conversation in history
        conversation_history[session_id].append({
            "role": "user",
            "content": user_message
        })
        conversation_history[session_id].append({
            "role": "assistant",
            "content": ai_response
        })

        # Limit history to prevent memory issues
        if len(conversation_history[session_id]) > 20:  # Keep last 10 exchanges
            conversation_history[session_id] = conversation_history[session_id][-20:]

        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({
                'response': ai_response,
                'session_id': session_id
            })
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        import traceback
        traceback.print_exc()

        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({
                'error': 'Internal server error',
                'details': str(e)
            })
        }
