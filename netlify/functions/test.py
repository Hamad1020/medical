def handler(event, context):
    """Simple test function"""
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json'
        },
        'body': '{"message": "Netlify functions are working!"}'
    }
