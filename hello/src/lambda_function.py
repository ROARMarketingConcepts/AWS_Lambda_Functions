import json

def lambda_handler(event, context):
    print(event)
    # TODO implement
    return {
        'statusCode': 200,
        'body': event  # json.dumps('Hello from Lambda!')
    }