import folium
from folium.plugins import MarkerCluster
import pandas as pd

def map_generator(request_id):
	start_point = [55.753766,37.621384]
	zoom_start	= 10
	map = folium.Map(location=start_point, zoom_start = zoom_start)
	marker_cluster = MarkerCluster().add_to(map)
	folium.CircleMarker(location=[55.900803, 37.528283], radius = 9, popup="info purple", fill_color="purple", color="gray", fill_opacity = 0.9).add_to(marker_cluster)
	folium.CircleMarker(location=[55.611109, 37.603445], radius = 9, popup="info green", fill_color="green", color="gray", fill_opacity = 0.9).add_to(marker_cluster)

	map.save("maps/"+request_id+".html")	
	with open("maps/"+request_id+".html","r") as file:
		return file.read()