import boto3

#Invoke the resource
my_dynamodb = boto3.resource('dynamodb')

#Create the table
table = my_dynamodb.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'Destination',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'Ranking',
            'AttributeType': 'N'
        },
    ],
    TableName='Top-Global-Tourist-Destinations',
    KeySchema=[
        {
            'AttributeName': 'Destination',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'Ranking',
            'KeyType': 'RANGE'
        },
    ],
    
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    },
    
)

#Printing table status
print("Table Status:", table.table_status)

#Connecting to DynamoDB
dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id='AKIAU27FDFMJCKHLBAH3',
    aws_secret_access_key='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',
    )
    
#Writing to DynamoDB

with table.batch_writer() as batch:
    batch.put_item(
        Item={
            'Destination': 'Auckland',
            'Ranking': '1',
           
        }
    )