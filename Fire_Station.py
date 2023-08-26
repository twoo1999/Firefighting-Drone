# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 01:51:51 2023

@author: taewoo
"""


import paho.mqtt.client as mqtt
import threading
import time
from tkinter import *
from tkinter import messagebox
import folium
import webbrowser
from haversine import haversine
from geopy.geocoders import Nominatim
import os

global lat_curr
global lon_curr
global lat
global lon
lat_curr = 37.670806
lon_curr = 126.778892

def setEntryText(lat, lon, addr, dist):
    et_lat_curr['state'] = 'normal'
    et_lon_curr['state'] = 'normal'
    et_address_curr['state'] = 'normal'
    et_dist_curr['state'] = 'normal'
    
    et_lat_curr.delete(0, "end")
    et_lon_curr.delete(0, "end")
    et_address_curr.delete(0, "end")
    et_dist_curr.delete(0, "end")

    et_lat_curr.insert(0, f"{lat}")
    et_lon_curr.insert(0, f"{lon}")
    et_address_curr.insert(0, f"{addr}")
    et_dist_curr.insert(0, f"{dist}km")

    et_lat_curr['state'] = 'readonly'
    et_lon_curr['state'] = 'readonly'
    et_address_curr['state'] = 'readonly'
    et_dist_curr['state'] = 'readonly'
    
def setButtonState(b):
    if(b):
        btn_map['state'] = NORMAL
        btn_start['state'] = NORMAL
        btn_cancel['state'] = NORMAL
    else:
        btn_map['state'] = DISABLED
        btn_start['state'] = DISABLED
        btn_cancel['state'] = DISABLED
def finish():
    root.destroy()
    root.quit()
    s_st.loop_stop()

def cancel():
    setEntryText("-", "-", "-", "-")
    os.remove("map.html")
    setButtonState(0)

def start():
    global lat
    global lon
    latitude = str(lat)
    longitude = str(lon)
    s_st.publish("data/Drone", (latitude + "," + longitude))
    lb_mission_curr.config(text='O')
    setButtonState(0)
    
def showMap():
    webbrowser.open("map.html")
    

def geocoding_reverse(lat, lon): 
    geolocoder = Nominatim(user_agent = 'South Korea', timeout=None)
    address = geolocoder.reverse(f"{lat}, {lon}")
    return address

def mqtt_s():
    s_st.loop_forever()
    
def call_back(client, userdata, message):
    global lat_curr
    global lon_curr
    global lat
    global lon
    string = str(message.payload.decode("utf-8"))
    cmd = string.split(",")
    if(cmd[0] == 'report'):
        address = geocoding_reverse(cmd[1], cmd[2])
        #print(type(address))
        lat = float(cmd[1])
        lon = float(cmd[2])
        m = folium.Map(location=[(lat+lat_curr)/2, (lon+lon_curr)/2], zoom_start=20)
        folium.Marker([lat_curr, lon_curr], popup='<b>Fire Station</b>').add_to(m)
        folium.Marker([lat, lon], popup='<b>Destination</b>').add_to(m)
        m.save("map.html")
        webbrowser.open("map.html")
        fireStation = (lat_curr, lon_curr)
        dest = (lat, lon)
        dist = str(round(haversine(fireStation, dest, unit = 'km'), 2))
        setEntryText(lat, lon, address, dist)
        setButtonState(1)
    
        messagebox.showinfo("report", "신고가 들어왔습니다.")
    elif(cmd[0] == "arriveDest"):
        lb_arrive_curr.config(text="O")
        messagebox.showinfo("Throw", "소화기를 투척합니다.")
    elif(cmd[0] == "arriveHome"):
        messagebox.showinfo("arrive", "드론이 복귀했습니다.")
        lb_arrive_curr.config(text="X")
        lb_mission_curr.config(text='X')
        cancel()
        # et_lat_curr['state'] = 'normal'
        # et_lon_curr['state'] = 'normal'
        # et_address_curr['state'] = 'normal'
        # et_dist_curr['state'] = 'normal'
        
        # et_lat_curr.insert(0, f"{lat}")
        # et_lon_curr.insert(0, f"{lon}")
        # et_address_curr.insert(0, f"{address}")
        # et_dist_curr.insert(0, f"{dist}km")

        # et_lat_curr['state'] = 'readonly'
        # et_lon_curr['state'] = 'readonly'
        # et_address_curr['state'] = 'readonly'
        # et_dist_curr['state'] = 'readonly'
        
     
        
        
        
        
    # command, latitude, longitude = string.split(",")
    # address = geocoding_reverse(latitude, longitude)
    # lat = float(latitude)
    # lon = float(longitude)
    
    # m = folium.Map(location=[(lat+lat_curr)/2, (lon+lon_curr)/2], zoom_start=15)
    # folium.Marker([lat_curr, lon_curr], popup='<b>Fire Station</b>').add_to(m)
    # folium.Marker([lat, lon], popup='<b>Destination</b>').add_to(m)
    # m.save("map.html")
    # webbrowser.open("map.html")
    # address = geocoding_reverse(latitude, longitude)
    # et_lat_curr['state'] = 'nomal'
    # et_lon_curr['state'] = 'nomal'
    # et_address_curr['state'] = 'noaml'
    # et_lat_curr.config(text=f"{lat}")
    # et_lon_curr.config(text=f"{lon}")
    # et_address_curr.config(text=f"{address}")

    # if(command == "report"):
    #     messagebox.showinfo("report", "there is report")
    #     if(msg == "yes"):
    #         s_st.publish("data/drone", (latitude + "," + longitude))
    #         frame.sett("on progress")
    #         frame.createLatitude(latitude)
    #         frame.createLongitude(longitude)
    # elif(string == "done"):
    #     messagebox.showinfo("info", "mission clear!")
    #     frame.sett("no progress")

 
    
# if __name__ == '__main__':
#     broker = "210.106.192.242"
#     s_st = mqtt.Client("mqtt_ST")
#     s_st.on_message = call_back
 
    
#     s_st.connect(broker, 1883)
#     s_st.subscribe("data/ST")
    
#     root = Tk()
#     root.title('GUI')
#     f1 = Frame(root, width=500, height=500)
#     f2 = Frame(root, width=500, height=500)
#     frame1 = Frame_1(f1)
#     frame2 = Frame_2(f2)
#     frame1.pack(side="left")
#   #  frame2.pack(side="right")
    
    
#     # t2 = threading.Thread(target=mqtt_s)
#     # t2.start()
    
    # root.mainloop()
#     # t2.join()
    # fireStation = (lat_curr, lon_curr)  #Latitude, Longitude

    # # 거리 계산
    # haversine(Seoul, Toronto, unit = 'km')
    
broker = "210.106.192.242"
s_st = mqtt.Client("mqtt_ST")
s_st.on_message = call_back
 
    
s_st.connect(broker, 1883)
s_st.subscribe("data/ST")
            
            # lb_lat_curr.insert(0, "asd")   
root = Tk()
root.title('GUI')
root.geometry("600x500")


lbFrame_place = LabelFrame(root, text = "위치 정보", pady = 20, padx = 20)
lbFrame_state = LabelFrame(root, text = "드론 상태", padx = 20, pady = 20)

locationFrame = Frame(lbFrame_place, width=500, height=500, padx=10)
addressFrame = Frame(locationFrame, width=500, height=500)
buttonFrame = Frame(lbFrame_place, width=500, height=500, pady=20)


lb_lat = Label(locationFrame, text="위도", width=10, height=2)
et_lat_curr = Entry(locationFrame, width=20)

et_lat_curr['state'] = "readonly"
et_lat_curr['readonlybackground'] = "white"

lb_lat.grid(row=0, column=0)
et_lat_curr.grid(row=0, column=1, sticky='w')



lb_lon = Label(locationFrame, text="경도", width=10, height=2)
et_lon_curr = Entry(locationFrame, width = 20)

et_lon_curr['state'] = "readonly"
et_lon_curr['readonlybackground'] = "white"

lb_lon.grid(row=1, column=0)
et_lon_curr.grid(row=1, column=1, sticky='w')



lb_dist = Label(locationFrame, text="거리", width=10, height=2)
et_dist_curr = Entry(locationFrame, width = 20)

et_dist_curr['state'] = "readonly"
et_dist_curr['readonlybackground'] = "white"

lb_dist.grid(row=2, column=0)
et_dist_curr.grid(row=2, column=1, sticky='w')



lb_address = Label(locationFrame, text="주소", width=10, height=2)
et_address_curr = Entry(locationFrame, text="-", width =52)

et_address_curr['state'] = "readonly"
et_address_curr['readonlybackground'] = "white"

lb_address.grid(row=3, column=0)
et_address_curr.grid(row=3, column=1)


locationFrame.pack(side='top')


btn_map = Button(buttonFrame, text="지도보기",width=10, command=showMap)
btn_start = Button(buttonFrame, text="드론 보내기",width=10, command=start)
btn_cancel = Button(buttonFrame, text="취소하기", width=10, command=cancel)

btn_map['state'] = DISABLED
btn_start['state'] = DISABLED
btn_cancel['state'] = DISABLED

btn_start.grid(row=0, column=0, padx=10, ipadx=5)
btn_cancel.grid(row=0, column=1, padx=10, ipadx=5)
btn_map.grid(row=0, column=2, padx=10, ipadx=5)

buttonFrame.pack(side='top')








lb_mission_curr = Label(lbFrame_state, text="X")
lb_mission = Label(lbFrame_state, text="미션 수행 중")

lb_mission.pack(side='left')
lb_mission_curr.pack(side='left')


lb_arrive_curr = Label(lbFrame_state, text="X")
lb_arrive = Label(lbFrame_state, text="드론 도착")

lb_arrive.pack(side='left')
lb_arrive_curr.pack(side='left')

lbFrame_place.pack(side='top', anchor=W, pady = 10, padx = 20)
lbFrame_state.pack(side='top', anchor=W, pady = 10, padx = 20)

btn_end = Button(root, text='종료', pady = 10, padx = 10, command=finish)
btn_end.pack(side='bottom', anchor=E, pady = 20, padx = 20)
t2 = threading.Thread(target=mqtt_s)
t2.start()
    
root.mainloop()
t2.join()



    
    
    
    # class MyFrame(Frame):
    #     def __init__(self, master=Frame):
    #         self.lb_dronestate = Label(master, text = "drone state : ")
    #         self.lb_curdronestate = Label(master, text = "nomal")
    #         self.lb_latitude= Label(master, text = "")
    #         self.lb_longitude = Label(master, text = "")
    #         self.lb_lat = Label(master, text = "Latitude : ")
    #         self.lb_long = Label(master, text = "Longitude : ")
    #         self.btn_map = Button(master, text = "지도 보기")
    #         self.lb_dronestate.place(x=20, y=50)
    #         self.lb_curdronestate.place(x=90, y=50)
    #         self.lb_lat.place(x=20, y=100)
    #         self.lb_latitude.place(x=90, y=100)
    #         self.lb_longitude.place(x=90, y=150)
    #         self.lb_long.place(x=20, y=150)
            
            
    #     def sett(self, text1):
    #         self.lb_curdronestate.config(text=text1)
            
    #     def createLatitude(self, pos):
    #         self.lb_latitude.config(text = pos)
            
    #     def createLongitude(self, pos):
    #         self.lb_longitude.config(text=pos)
        
            
    # class Frame_1(Frame):
    #     def __init__(self, master=Frame):
    #         self.lb_lat = Label(master, text="Latitude")
    #         self.lb_lon = Label(master, text="Longitude")
    #         self.lb_lat_curr = Label(master, text="")
    #         self.lb_lon_curr = Label(master, text="")
    #         self.lb_state_curr = Label(master, text="Not Yet")
    #         self.lb_state = Label(master, text="Drone")
            
    #         self.lb_lat.grid(row=0,column=0)
    #         self.lb_lat_curr.grid(row=0,column=1)
            
    #         self.lb_lon.grid(row=1,column=0)
    #         self.lb_lon_curr.grid(row=1,column=1)
            
    #         self.lb_state.grid(row=2,column=0)
    #         self.lb_state_curr.grid(row=2,column=1)

    #     def setText(self, lb, msg):
    #         lb.config(text=msg)
            
    # class Frame_2(Frame):
    #     def __init__(self, master=Frame):
    #         self.btn_map = Button(master, text="지도보기")
    #         self.btn_start = Button(master, text="드론 출발")
            
    #         self.btn_map.grid(row= 0 , column = 0)
    #         self.btn_start.grid(row= 1 , column = 0)
         
    # def geocoding_reverse(lat, lon): 
    #     geolocoder = Nominatim(user_agent = 'South Korea', timeout=None)
    #     address = geolocoder.reverse(f"{lat}, {lon}")

    #     return address