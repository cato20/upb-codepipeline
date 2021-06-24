import json
import boto3
import os


users_table = os.environ['USERS_TABLE']

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(users_table)

def getUser(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    
    path = event["path"]
    array_path = path.split("/")
    user_id =array_path[-1]
    
    response = table.get_item(
        Key={
            'pk': user_id,
            'sk': 'age'
        }
    )
    item = response['Item']
    print(item)
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }
    
def putUser(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    array_path = path.split("/")
    user_id =array_path[-1]
    body = event["body"]
    bodyObject = json.loads(body)
    table.put_item(
        Item={
            'pk': user_id,
            'sk': 'age',
            'name': bodyObject['name'],
            'last_name': bodyObject['last_name'],
            'age': bodyObject['age']
        }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
