# Disaster Recovery

## What is Disaster Recovery Plan?

- A process used by companies to anticipate and address any technology problems that may happen. Companies use DR to recover quickly from any damaging events such as power outage or security issues.

## Benefits of Disaster Recovery Plan?

- Ensures business continuity

- Enhances system security

- Improves customer retention

- Reduces recovery costs

## What is S3?

- S3 (Amazon Simple Storage Service) is an object storage service that offers industry-leading scalability, data availability, security, and performance.

- Bucket stands for Folder
- Object stands for Files

## What is AWS CLI?

- The AWS Command Line Interface (AWS CLI) is a tool to manage your AWS services. You can control multiple AWS services from the command line and automate them through scripts.

- Need AWS Acess & Secret Keys in EC2 instance.

## What is AWS SDK?

- SDK (Software Development Kit) is a set of platform building tools for developers. They contain components for debugging and libraries to create code for a programming language or operating system.

- Example of SDK is `boto3`.

# Connect AWS CLI to S3

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
