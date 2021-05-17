import boto3 

ec2client = boto3.client('ec2', "us-east-1")
instanceresponse = ec2client.describe_instances()
for reservation in instanceresponse["Reservations"]:
    for instance in reservation["Instances"]:
        print(instance["InstanceId"])

        ##repeat for each resource 
