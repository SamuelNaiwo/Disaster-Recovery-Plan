# Disaster Recovery

### What is Disaster Recovery Plan?

- A process used by companies to anticipate and address any technology problems that may happen. Companies use DR to recover quickly from any damaging events such as power outage or security issues.

### Benefits of Disaster Recovery Plan?

- Ensures business continuity

- Enhances system security

- Improves customer retention

- Reduces recovery costs

### What is S3?

- S3 (Amazon Simple Storage Service) is an object storage service that offers industry-leading scalability, data availability, security, and performance.

- Bucket stands for Folder
- Object stands for Files

### What is AWS CLI?

- The AWS Command Line Interface (AWS CLI) is a tool to manage your AWS services. You can control multiple AWS services from the command line and automate them through scripts.

- Need AWS Acess & Secret Keys in EC2 instance.

### What is AWS SDK?

- SDK (Software Development Kit) is a set of platform building tools for developers. They contain components for debugging and libraries to create code for a programming language or operating system.

- Example of SDK is `boto3`.

## Connect AWS CLI to S3

1.	Create a new instance with port 22 open.

2.	Open your terminal/bash window.
3.	Change directory into .ssh folder. `cd .ssh`
4.	Paste ssh key from AWS into terminal to ssh into instance.
5.	Run the following command to update your instance. `sudo apt update -y`
6.	Run the following command to upgrade your instance. `sudo apt upgrade -y`
7.	Check python version `python3 --version`. I needed 3.6 or above.
8.	Install python on your instance. `sudo apt install python`
9.	Install pip on your instance. `sudo apt install python3-pip`
10.	Create a environment variable to tell ubuntu which version of python to use `alias python=3`
11.	Install AWS CLI onto your instance. `sudo python3 -m pip install awscli`
12.	Run the command `aws configure` to enter specific details.
13.	Copy and paste your Access Key ID which can be found in your file in your .ssh folder.
14.	Copy and paste your Secret Access Key which can be found in your file in your .ssh folder.
15.	Enter your default region. I used `eu-west-1`
16.	Enter your output format. I used `json`
17.	Validate your connection to your S3 bucket by testing to see if you can see the objects inside. `aws s3 ls`. If prompted with error, follow from step 12 to configure again.

# S3 Bucket

## Create S3 Bucket

1. Create a bucket/folder `aws s3 mb s3://samuel-tech221`

2. Check if bucket was created `aws s3 ls`
3. Create and open a file `sudo nano test.txt`
4. Save file `ctl + x` and `y` to confirm. Then `enter` to exit.
5. Check if file is created `ls`
6. Copy file to your folder. `aws s3 cp test.txt s3//samuel-tech221`
7. Move file from S3 bucket to instance
`aws s3 cp s3://Samuel-tech221/test.txt /home/ubuntu`
8. Delete file from s3 bucket `aws s3 cp s3://samuel-tech221/test.txt`
9. Remove s3 bucket `aws s3 rb s3://samuel-tech221/test.txt`

## S3 Storages Classes

- S3 Standard (S3 Standard)

- S3 Intelligent-Tiering (S3 Intelligent-Tiering)
- S3 Standard-Infrequent Access (S3 Standard-IA)
- S3 One Zone-Infrequent Access (S3 One Zone-IA)

### Archive

- Amazon S3 Glacier Instant Retrieval

- S3 Glacier Flexible Retrieval (Formerly S3 Glacier)
- S3 Glacier Deep Archive

# Boto3 and S3

## Create S3 Bucket

1. Download boto3 onto your instance. `pip3 install boto3`

2. Create a new python file `sudo nano create_bucket.py`

3. Enter this script into your python file:

```
import boto3

AWS_REGION = "eu-west-1"
client = boto3.client("s3", region_name=AWS_REGION)

bucket_name = "samuel-tech221"
location = {'LocationConstraint': AWS_REGION}

response = client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
```

4. Run the following command in your terminal to run the file `python3 create_bucket.py`

## Upload file to S3 Bucket.

1. Create a new python file `sudo nano upload_file.py`

2. Enter this script into your python file:

```
import boto3

client = boto3.client('s3')
s3 = boto3.resource('s3')

bucket_name="samuel-tech221"

s3.Bucket(bucket_name).upload_file('/home/ubuntu/test.txt', 'test.txt')
```

3. Run the following command in your terminal to upload a file. `python3 upload_file.py`

## Download file from S3 Bucket.

1. Create a new python file `sudo nano download_file.py`

2. Enter this script into your python file:

```
import boto3

client = boto3.client('s3')
s3 = boto3.resource('s3')

bucket_name="samuel-tech221"

s3.download_file(bucket_name, 'test.txt', 'test.txt')
```

3. Run the following command in your terminal to upload a file. `python3 download_file.py`

## Delete file from S3 Bucket.

1. Create a new python file `sudo nano delete_file.py`

2. Enter this script into your python file:

```
import boto3

client = boto3.client('s3')
s3 = boto3.resource('s3')

bucket_name="samuel-tech221"

s3.Object(bucket_name, 'test.txt').delete()
```

3. Run the following command in your terminal to upload a file. `python3 delete_file.py`

## Delete S3 Bucket.

1. Create a new python file `sudo nano delete_bucket.py`

2. Enter this script into your python file:

```
import boto3

client = boto3.client('s3')
s3 = boto3.resource('s3')

bucket_name="samuel-tech221"

response = client.delete_bucket(
        Bucket=bucket_name,
)
```

3. Run the following command in your terminal to upload a file. `python3 delete_file.py`