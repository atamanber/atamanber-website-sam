import boto3
import json
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('atamanber-stats')

def lambda_handler(event, context):
    
    response = table.query(
        KeyConditionExpression=Key('stat').eq('visitor-count')
        )
    count = response['Items'][0]['quantity']
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Credentials': '*',
            'Content-Type': 'application/json'
        },
        'body': count
    }