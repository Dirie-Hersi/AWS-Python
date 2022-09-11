import boto3


# Get the service resource.
dynamodb = boto3.resource('dynamodb')


table = dynamodb.Table('Top-Global-Tourist-Destinations')

with table.batch_writer() as batch:
    batch.put_item(
        Item={
            'Destination': 'Auckland',
            'Ranking': 1,
        }
    )
    batch.put_item(
        Item={
            'Destination': 'Taipei',
            'Ranking': 2,
        }
    )
    batch.put_item(
        Item={
            'Destination': 'Freiburg',
            'Ranking': 3,
        }
    )
    batch.put_item(
        Item={
            'Destination': 'Atlanta',
            'Ranking': 4,
        }
    )
    batch.put_item(
        Item={
            'Destination': 'Lagos',
            'Ranking': 5,
        }
    )
    batch.put_item(
        Item={
            'Destination': 'Nicosia',
            'Ranking': 6,
        }
    )
    batch.put_item(
        Item={
            'Destination': 'Dublin',
            'Ranking': 7,
        }
    )
    batch.put_item(
        Item={
            'Destination': 'Merida',
            'Ranking': 8,
        }
    )
    batch.put_item(
        Item={
            'Destination': 'Florence',
            'Ranking': 9,
        }
    )
    batch.put_item(
        Item={
            'Destination': 'Gyeongju',
            'Ranking': 10,
        }
    )


print("Items Successfully Added")