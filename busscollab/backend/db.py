import boto3
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Optional: if you want to use .env credentials (recommended for local dev)
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

# Create DynamoDB connection
if AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY:
    dynamodb = boto3.resource(
        "dynamodb",
        region_name=AWS_REGION,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )
else:
    # Use default AWS credentials (CLI or environment)
    dynamodb = boto3.resource(
        "dynamodb",
        region_name=AWS_REGION
    )

# Table name (you can also move this to .env)
TABLE_NAME = os.getenv("DYNAMODB_TABLE", "inventory_items")

# Reference table
table = dynamodb.Table(TABLE_NAME)


# ✅ Helper function: Get all items
def get_all_items():
    try:
        response = table.scan()
        return response.get("Items", [])
    except Exception as e:
        return {"error": str(e)}


# ✅ Helper function: Add item
def add_item(item):
    try:
        table.put_item(Item=item)
        return {"message": "Item added successfully"}
    except Exception as e:
        return {"error": str(e)}