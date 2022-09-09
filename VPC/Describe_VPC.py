import boto3
import json


client = boto3.client('ec2')

response = client.describe_vpcs()
totalvpcs = response["Vpcs"]

print("The total number of VPCs is:", len(totalvpcs))

for vpc in totalvpcs:
    print(vpc["VpcId"])
    
print()

print(json.dumps(response, indent=2, default=str))

print()
