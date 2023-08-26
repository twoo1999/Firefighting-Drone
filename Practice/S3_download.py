import boto3
accessKey = 'AKIAZDLFNYZT2RCQNA5G'
secretKey = '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'
region = 'ap-northeast-2'
bucket_name = 'twootest'
prefix = 'test/'

bucket_name = "twootest"
in_file = 'aaa.jpg'

out_file = 'test.jpg'

s3 = boto3.client('s3', aws_access_key_id = accessKey, aws_secret_access_key=secretKey, region_name=region)

# 버킷 이름, 버킷 내 파일 경로, 받아올 이름름
s3.download_file(bucket_name, 'test/'+out_file, in_file)