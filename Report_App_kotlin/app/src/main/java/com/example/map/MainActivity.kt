package com.example.map
//210.106.192.242
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.TextView
import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken
import org.eclipse.paho.client.mqttv3.MqttCallback
import org.eclipse.paho.client.mqttv3.MqttClient
import org.eclipse.paho.client.mqttv3.MqttMessage

class MainActivity : AppCompatActivity() {

    val ServerIP:String = "tcp://210.106.192.242:1883"  //1번 서버 IP
    val TOPIC:String = "data/ST"	//2번 토픽

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val tv_lat : TextView = findViewById(R.id.tv_lat)
        val tv_long : TextView = findViewById(R.id.tv_long)
        val btn_send : Button = findViewById(R.id.btn_send)

        var mqttClient: MqttClient? = null
        mqttClient = MqttClient(ServerIP, MqttClient.generateClientId(), null) //3번 연결설정
        mqttClient.connect()

        btn_send.setOnClickListener{
            mqttClient.publish(TOPIC,MqttMessage(("report"+"," +(tv_lat.text as String) + "," +(tv_long.text as String)).toByteArray()))
//            mqttClient.publish(TOPIC, MqttMessage((tv_lat.text as String).toByteArray()))
//            mqttClient.publish(TOPIC, MqttMessage((tv_long.text as String).toByteArray()))
        }

        mqttClient.setCallback(object : MqttCallback { //6번 콜백 설정
            override fun connectionLost(p0: Throwable?) {
                //연결이 끊겼을 경우
                Log.d("MQTTService","Connection Lost")
            }
            override fun messageArrived(p0: String?, p1: MqttMessage?) {
                //메세지가 도착했을 때 여기
                Log.d("MQTTService","Message Arrived : " + p1.toString()) //7번 메세지 도착
            }
            override fun deliveryComplete(p0: IMqttDeliveryToken?) {
                //메세지가 도착 하였을 때
                Log.d("MQTTService","Delivery Complete")
            }
        })

        if(intent.hasExtra("pos")){
            val pos = (intent.getStringExtra("pos"))?.split(",")
            tv_lat.text = pos?.get(0)
            tv_long.text = pos?.get(1)
        }

    }
}

