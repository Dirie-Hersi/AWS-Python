import boto3

s3 = boto3.client("s3")

s3.delete_object(Bucket="my-first-bucket-dhersi-us1-3", Key="file1.txt")
print("File deleted")


#Delete Multiple Objects
#objects = s3.list_objects(Bucket = "my-first-bucket-dhersi-us1-3")["Contents"]
#for object in objects:
    #print(object["Key"])
    #s3.delete_object(Bucket = "my-first-bucket-dhersi-us1-3", Key = object["Key"])
    
