import boto3

response = client.create_queue(
    QueueName='Test',
    
)

print(response)