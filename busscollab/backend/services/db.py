import boto3

# Create DynamoDB connection
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# Reference your table
table = dynamodb.Table('inventory_items')