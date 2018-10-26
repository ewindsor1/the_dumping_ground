import boto3


s3 = boto3.resource('s3')
# Upload a new file
print('opening a file to read')
data = open('/home/ec2-user/environment/billshock/test/testdata1.txt', 'rb')
s3.Bucket('emmatest1').put_object(Key='testdata1.txt', Body=data)