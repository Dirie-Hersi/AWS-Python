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