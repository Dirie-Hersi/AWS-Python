import boto3


# Get the service resource.
dynamodb = boto3.resource('dynamodb')

response = dynamodb.scan()