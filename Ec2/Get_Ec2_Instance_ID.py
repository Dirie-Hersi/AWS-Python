import boto3
import json

ec2_client = boto3.resource("ec2")

instances = ec2_client.instances.all()

for instance in instances:
    print(f'EC2 instance {instance.id}" information:')
    print(f'Instance state: {instance.state["Name"]}')
    print(f'Instance AMI: {instance.image.id}')
    print(f'Instance platform: {instance.platform}')
    print(f'Instance type: "{instance.instance_type}')
    print(f'Piblic IPv4 address: {instance.public_ip_address}')
    print('-'*60)
