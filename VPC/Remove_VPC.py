import boto3

client = boto3.client('ec2')

response = client.delete_vpc(
    VpcId='vpc-00443c8306be04531',
    
)

print("VPC is deleted")