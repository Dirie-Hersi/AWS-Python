import boto3

dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id='AKIAU27FDFMJCKHLBAH3',
    aws_secret_access_key='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',
    )
    
#Writing to DynamoDB

with dynamodb.batch_writer() as batch:
    batch.put_item(
        Item={
            'Destination': 'Auckland',
            'Ranking': '1',
           
        }
    )