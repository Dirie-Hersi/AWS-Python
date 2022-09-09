import boto3

myclient= boto3.client("ec2")

myclient.create_vpc(CidrBlock = '10.0.0.0/16')

print("New VPC Successfully Created")