import boto3# Get the service resource.
dynamodb = boto3.resource('dynamodb')#Getting the response and generating a scan
table = dynamodb.Table('Top-Global-Tourist-Destinations')
response = table.scan()
data = response['Items']#Loop to print out items
for item in data:
    print(item)
    print('-'*60)