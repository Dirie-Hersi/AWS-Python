import boto3

s3 = boto3.client('s3')

s3.list_objects(Bucket="my-first-bucket-dhersi-us1-3")

objects = s3.list_objects(Bucket="my-first-bucket-dhersi-us1-3") ["Contents"]

print(objects)

for object in objects:
    print(object["Key"])
    print(object["LastModified"])