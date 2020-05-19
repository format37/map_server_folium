import folium
from folium.plugins import MarkerCluster
import pandas as pd
import pymssql

def connect_sql(database):
	sql_login='ICECORP\\1c_sql'
	sql_pass='dpCEoF1e4A6XPOL'
	return pymssql.connect(server='10.2.4.124', user=sql_login, password=sql_pass, database=database)

def read_data(request_id):
	conn = connect_sql('geo_map')
	cursor = conn.cursor()
	query ="show tables;"
	cursor.execute(query)
	data = []
	for row in cursor.fetchall():
		id	= row[0]
	record	= {
		'lat':55.900803,
		'lon':37.528283,
		'info':'info',
		'color':'gray',
		'fill_color','purple',
		'fill_opacity',0.9
		}
	data.append(record)
	return data
	
	
def map_generator(request_id):
	start_point = [55.753766,37.621384]
	zoom_start	= 10
	map = folium.Map(location=start_point, zoom_start = zoom_start)
	marker_cluster = MarkerCluster().add_to(map)
	data = read_data(request_id)
	for record in data:
		folium.CircleMarker(
			location=[record['lat'], 
			record['lon']], 
			radius = 9, 
			popup=record['info'], 
			fill_color=record['fill_color'], 
			color=record['color'], 
			fill_opacity = record['fill_opacity']
		).add_to(marker_cluster)
	#folium.CircleMarker(location=[55.900803, 37.528283], radius = 9, popup="info purple", fill_color="purple", color="gray", fill_opacity = 0.9).add_to(marker_cluster)
	#folium.CircleMarker(location=[55.611109, 37.603445], radius = 9, popup="info green", fill_color="green", color="gray", fill_opacity = 0.9).add_to(marker_cluster)

	map.save("maps/"+request_id+".html")	
	with open("maps/"+request_id+".html","r") as file:
		return file.read()