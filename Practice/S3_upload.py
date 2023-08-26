import boto3
accessKey = 'AKIAZDLFNYZT2RCQNA5G'
secretKey = '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'
region = 'ap-northeast-2'
bucket_name = 'twootest'
prefix = 'test/'

in_file = 'test.jpg'

out_file = in_file

s3 = boto3.client('s3', aws_access_key_id = accessKey, aws_secret_access_key=secretKey, region_name=region)

# 업로드할 파일 이름, 버킷 이름 ,버킷 내 경로
s3.upload_file(in_file, bucket_name, 'test/'+out_file)

