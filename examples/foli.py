import folium

map = folium.Map(location=[37.296933,-121.9574983], zoom_start = 8)

#folium.Marker(location=[37.4074687,-122.086669], popup = "Google HQ", icon=folium.Icon(color = 'gray')).add_to(map)
for coordinates in [[37.4074687,-122.086669],[37.8199286,-122.4804438]]:
    #folium.Marker(location=coordinates, popup = str(coordinates), icon=folium.Icon(color = 'green')).add_to(map)
    folium.CircleMarker(location=coordinates, radius = 9, popup=str(coordinates), fill_color="blue", color="gray", fill_opacity = 0.9).add_to(map)

map.save("map1.html")
