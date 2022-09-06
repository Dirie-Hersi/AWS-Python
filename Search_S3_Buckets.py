import boto3

#Listing buckets
resource = boto3.resource("s3")
print(list(resource.buckets.all()))


#Searching bucket names using a loop
for bucket in resource.buckets.all():
    print(bucket.name)
    
#Total number of buckets
print(len(list(resource.buckets.all())))

#Bucket  info
s3_resource=boto3.client("s3")
print(s3_resource.list_buckets()["Buckets"])

print()

#Info of individual bucket
print(s3_resource.list_buckets()["Buckets"] [0]["CreationDate"])

print()

#In a loop
for bucket in s3_resource.list_buckets()["Buckets"]:
    print(bucket["Name"])
    print(bucket["CreationDate"])