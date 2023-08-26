import paho.mqtt.client as mqtt
import boto3
accessKey = 'AKIAZDLFNYZT2RCQNA5G'
secretKey = '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'
region = 'ap-northeast-2'
bucket_name = 'twootest'
prefix = 'test/'
broker = '210.106.192.242'
cnt = 1
#in_file = 'test.jpg'
#out_file = 'test.jpg'


def on_message(client, userdata, message):
    global cnt
    in_file = 'test'+str(cnt) +'.jpg'
    cnt+=1
    string = str(message.payload.decode('utf-8'))
    s3.download_file(bucket_name, 'test/' + string, in_file)
    s_st.publish("data2", "down success")
    
    








s_st = mqtt.Client("mqtt")
#s_st.on_message = call_back
s3 = boto3.client('s3', aws_access_key_id = accessKey, aws_secret_access_key=secretKey, region_name = region)
s_st.connect(broker, 1883)
s_st.on_message = on_message
s_st.subscribe("data")


s_st.loop_forever()