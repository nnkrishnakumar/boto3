import boto3
aws_mangement_console=boto3.session.Session(profile_name='default')
print(dir(aws_mangement_console)) # dir() function is of python function to see all the function and magic method to see 
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
# '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
#'__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_loader', '_register_default_handlers', '_session', '_setup_loader',
# 'available_profiles', 'client', 'events', 'get_available_partitions', 'get_available_regions', 'get_available_resources', 
#'get_available_services', 'get_credentials', 'get_partition_for_region', 'profile_name', 'region_name', 'resource', 'resource_factory']

# now to see all the available resource we have a function in dir() get_available_resource()

print(aws_mangement_console.get_available_resources())  


# Output:   ['cloudformation', 'cloudwatch', 'dynamodb', 'ec2', 'glacier', 'iam', 'opsworks', 's3', 'sns', 'sqs']
# the above all are the resouce object we have in aws mangement console
