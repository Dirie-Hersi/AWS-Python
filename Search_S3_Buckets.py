import boto3

#Listing buckets
resource = boto3.resource("s3")
print(list(resource.buckets.all()))


#Searching bucket names using a loop
for bucket in resource.buckets.all():
    print(bucket.name)
    
#Total number of buckets
print(len(list(resource.buckets.all())))

#Bucket creation info
s3_resource=boto3.client("s3")
print(s3_resource.list_buckets()["Buckets"])