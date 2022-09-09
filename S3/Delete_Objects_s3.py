import boto3

s3 = boto3.client("s3")

s3.delete_object(Bucket="my-first-bucket-dhersi-us1-3", Key="file1.txt")

print("File deleted")