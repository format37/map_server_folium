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
	query = "SELECT lat,lon,info,color,fill_color,fill_opacity FROM geo_map.dbo.requests where request_id='"+request_id+"';"
	cursor.execute(query)
	data = []
	for row in cursor.fetchall():
		record	= {
			'lat':row[0],
			'lon':row[1],
			'info':row[2],
			'color':row[3],
			'fill_color':row[4],
			'fill_opacity':row[5]
			}
		data.append(record)
	conn.close()
	
	return data
	
	
def map_generator(request_id,lat,lon,zoom):
	start_point = [lat,lon]
	zoom_start	= zoom
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
		
	'''conn = connect_sql('geo_map')
	cursor = conn.cursor()
	query ="delete from geo_map.dbo.requests where request_id='"+request_id+"';"
	cursor.execute(query)
	conn.commit()
	conn.close()'''
		
	map.save("maps/"+request_id+".html")	
	with open("maps/"+request_id+".html","r") as file:
		return file.read()