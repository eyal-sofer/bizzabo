import boto3

region = "us-east-1"
input_string = input('Enter resources you wish to list, separated by space ')
print("\n")
resource_list = input_string.split()
# print list
print('resource list: ', resource_list)

# convert each item to int type
for i in range(len(resource_list)):
    client = boto3.client(resource_list[i], region)
    instanceresponse = client.describe_instances()
    for reservation in instanceresponse["Reservatsions"]:
        for instance in reservation["Instances"]:
            print(instance["InstanceId"])
