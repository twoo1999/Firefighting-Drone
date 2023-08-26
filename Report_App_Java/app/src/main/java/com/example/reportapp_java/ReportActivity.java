package com.example.reportapp_java;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;

public class ReportActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_report);
//        Intent intent = getIntent();
//        Log.i("Test", "sdsd");
//        String loc = intent.getStringExtra("location");
//        String[] locArr = loc.split(",");
//        Log.i("Test", "sdsd");
////        TextView tv_latStatus = findViewById(R.id.tv_latStatus);
////        TextView tv_lonStatus = findViewById(R.id.tv_lonStatus);
//        Log.i("Test", "sdsd");
////        tv_latStatus.setText(locArr[0]);
////        tv_lonStatus.setText(locArr[1]);
//        //TextView tv = findViewById(R.id.tv);
//        Log.i("Test", "sdsd");
//        try {
//            MqttClient client = new MqttClient("tcp://210.106.192.242:1883", MqttClient.generateClientId(),null);
//            client.connect();
//            Log.i("Test", "connect");
//            client.publish("data/ST", new MqttMessage(loc.getBytes()));
//            //tv.setText("신고가 완료됐습니다.");
//
//        } catch (MqttException e) {
//            e.printStackTrace();
//        }

    }
}