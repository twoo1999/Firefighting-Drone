
import folium
import webbrowser

m = folium.Map(location=[37.53897093698831, 127.05461953077439], zoom_start=20)

folium.Marker([37.53897093698831, 127.05461953077439]).add_to(m)
m.save("map.html")
webbrowser.open("map.html")