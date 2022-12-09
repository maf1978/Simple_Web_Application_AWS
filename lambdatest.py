import json

def lambda_handler(event, context):
    name = event['firstname'] +' '+ event['lastname']

    return {
    'statusCode': 200,
    'body': json.dumps('Hello from Lambda, ' + name)
    }

    
