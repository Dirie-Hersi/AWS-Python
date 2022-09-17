import boto3
import json

mysqs = boto3.client('sqs')

response = mysqs.create_queue(
    QueueName='My_Queue',
    
)

print(json.dumps(response, indent=2, default=str))