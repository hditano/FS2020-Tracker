import folium
import os


my_array = []
#os.remove('my_map4.html')

def Marker(latlon):
    
    my_map4 = folium.Map(location = [latlon[0], latlon[1]], zoom_start= 12)
    
    folium.Marker(latlon, popup=f'{latlon}').add_to(my_map4)
    
    place_lat = [latlon[0]]
    place_lon = [latlon[1]]

    for i in range(len(place_lat)):
        my_array.append([place_lat[i], place_lon[i]])

  
    folium.PolyLine(my_array, color='red', line_opacity = 0.5).add_to(my_map4)

    my_map4.save("my_map4.html")

