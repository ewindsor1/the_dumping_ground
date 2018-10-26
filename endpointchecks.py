import boto3
import json


sagemaker = boto3.client('sagemaker-runtime')

a = "0,99,33,179.1,93,238.3,102,165.7,96,10.6,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1"



response = sagemaker.invoke_endpoint(
    EndpointName='EmmaTest1',
    ContentType='text/csv',
    Body=a
)

print (response)
result = json.loads(response['Body'].read().decode())


print (result)

print("Our actual prediction is")
print (round (result,0))
