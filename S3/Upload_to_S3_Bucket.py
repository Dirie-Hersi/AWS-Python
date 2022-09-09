import boto3

s3 = boto3.resource('s3')
s3.Bucket ('my-first-bucket-dhersi-us1-3').upload_file('/home/ec2-user/environment/dhersi-aws-python_scripts/file2.txt', 'file2.txt')