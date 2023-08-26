package com.example.map

import android.annotation.SuppressLint
import android.content.Intent
import android.content.pm.PackageManager
import android.location.Location
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.Looper
import android.widget.Button
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat

import com.google.android.gms.maps.CameraUpdateFactory
import com.google.android.gms.maps.GoogleMap
import com.google.android.gms.maps.OnMapReadyCallback
import com.google.android.gms.maps.SupportMapFragment
import com.google.android.gms.maps.model.LatLng
import com.google.android.gms.maps.model.MarkerOptions
import com.example.map.databinding.ActivityMapsBinding
import com.google.android.gms.location.*
import com.google.android.gms.maps.model.CameraPosition

class MapsActivity : AppCompatActivity(), OnMapReadyCallback {

    val permissions = arrayOf(android.Manifest.permission.ACCESS_FINE_LOCATION, android.Manifest.permission.ACCESS_COARSE_LOCATION)
    val PERM_FLAG = 99
    private lateinit var mMap: GoogleMap
    private lateinit var binding: ActivityMapsBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
//        val btn_location : Button = findViewById(R.id.btn_location)
        setContentView(R.layout.activity_maps)
        val btn_location : Button = findViewById(R.id.btn_location)


        if(isPermitted()){
            startProcess()
        } else{
            ActivityCompat.requestPermissions(this, permissions, PERM_FLAG)
        }
        btn_location.setOnClickListener{
            val intent = Intent(this, MainActivity::class.java)
            val pos : String = (LastLocation.latitude).toString() + "," + (LastLocation.longitude).toString()
            intent.putExtra("pos", pos)
            startActivity(intent)
            finish()
        }
    }

    fun isPermitted() : Boolean{
        for(perm in permissions){
            if(ContextCompat.checkSelfPermission(this, perm) != PackageManager.PERMISSION_GRANTED)
                return false
        }
        return true
    }

    fun startProcess(){
        val mapFragment = supportFragmentManager // 맵 프래그먼트 관리 변수 설정
            .findFragmentById(R.id.map) as SupportMapFragment
        mapFragment.getMapAsync(this) // 맵 등록 -> 띄우기
    }

    override fun onMapReady(googleMap: GoogleMap) {
        mMap = googleMap

        fusedLocationClient = LocationServices.getFusedLocationProviderClient(this)
        setUpdateLocationListener()
    }

    lateinit var fusedLocationClient: FusedLocationProviderClient // 배터리 소모 좋아지고 정확한 좌표값을 가져옴
    lateinit var LastLocation: Location // 위치 값을 가지고 있는 객체

    @SuppressLint("MissingPermission") // 문법검사기
    fun setUpdateLocationListener(){
        val locationReqeust = LocationRequest.create().apply{
            priority = LocationRequest.PRIORITY_HIGH_ACCURACY
        }

        // 로케이션 요청 함수 호출(locationRequest, locatiobCallback을 담아 보낸다)
        fusedLocationClient.requestLocationUpdates(locationReqeust, locationCallback, Looper.myLooper())
    }
    private val locationCallback = object : LocationCallback(){
        override fun onLocationResult(locationResult: LocationResult) {
            // 시스템에서 받은 location 정보를 onLocationChanged()에 전달
            locationResult.lastLocation
            onLocationChanged(locationResult.lastLocation)
            moveToLocation(locationResult.lastLocation)
        }
    }

    fun onLocationChanged(location: Location){
        LastLocation = location

        println(location.latitude)
        println(location.longitude)

    }

    fun moveToLocation(location : Location){
        val myLocation = LatLng(location.latitude, location.longitude)
        val marker = MarkerOptions()
            .position(myLocation)
            .title("I am here")
        val cameraOption = CameraPosition.Builder()
            .target(myLocation)
            .zoom(15.0f)
            .build()
        val camera = CameraUpdateFactory.newCameraPosition(cameraOption)
        mMap.clear()
        mMap.addMarker(marker)
        mMap.moveCamera(camera) // 카메라 위치 이동하는 함수
    }

}