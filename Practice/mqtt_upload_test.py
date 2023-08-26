import paho.mqtt.client as mqtt
import boto3
import time
accessKey = 'AKIAZDLFNYZT2RCQNA5G'
secretKey = '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'
region = 'ap-northeast-2'
bucket_name = 'twootest'
prefix = 'test/'

def on_message(client, userdata, message):
    string = str(message.payload.decode('utf-8'))
    print(string)

broker = '210.106.192.242'
s_st = mqtt.Client('ss')

s_st.connect(broker, 1883)
s_st.on_message = on_message
s_st.subscribe('data2')
s3 = boto3.client('s3', aws_access_key_id = accessKey, aws_secret_access_key=secretKey, region_name=region)


#in_file = 'test.jpg'

#out_file = in_file



# 업로드할 파일 이름, 버킷 이름 ,버킷 내 경로

for i in range(5):
    in_file = 'test'+str(i+1)+'.jpg'
    out_file = in_file
    s3.upload_file((in_file), bucket_name, 'test/'+out_file)
    s_st.publish("data", out_file)
    time.sleep(5)







s_st.loop_forever()