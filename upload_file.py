import boto3

client = boto3.client('s3')
s3 = boto3.resource('s3')

bucket_name="samuel-tech221"

s3.Bucket(bucket_name).upload_file('/home/ubuntu/test.txt', 'test.txt')

print('File uploaded')