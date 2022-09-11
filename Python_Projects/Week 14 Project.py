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
    ],
    TableName='Top_Global_Tourist_Destinations',
    KeySchema=[
        {
            'AttributeName': 'Destination',
            'KeyType': 'HASH'
        },
    ],
    
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    },
    
)
#Printing table status
print("Table Status", table.table_status)


#Add 10 items to the table
