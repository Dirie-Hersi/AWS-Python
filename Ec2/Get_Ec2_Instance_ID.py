import boto3

#Using both resource and client
ec2_client = boto3.resource("ec2")
ec2= boto3.client("ec2")


#Printing total number of Ec2
number = ec2.describe_instances()
total_number = len(number["Reservations"])
print(f"You currently have {total_number} Ec2 instances")

print()

#resource variable
instances = ec2_client.instances.all()

#loop to get ec2 data
for instance in instances:
    print(f'EC2 instance {instance.id}" information:')
    print(f'Instance state: {instance.state["Name"]}')
    print(f'Instance AMI: {instance.image.id}')
    print(f'Instance platform: {instance.platform}')
    print(f'Instance type: "{instance.instance_type}')
    print(f'Piblic IPv4 address: {instance.public_ip_address}')
    print('-'*60)
