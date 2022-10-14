from aiohttp import web
import os
import folium
from folium.plugins import MarkerCluster
import pandas as pd
from io import StringIO
import logging
import numpy as np


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


async def call_test(request):
	content = "get ok"
	return web.Response(text=content,content_type="text/html")


def map_generator(df,zoom_start=10):
	start_point = [df.iloc[0].lat,df.iloc[0].lon]
	map = folium.Map(location=start_point, zoom_start = zoom_start)
	marker_cluster = MarkerCluster().add_to(map)
	for idx, row in df.iterrows():
		folium.CircleMarker(
			location=[row['lat'], 
			row['lon']], 
			radius = 9, 
			popup=row['info'], 
			fill_color=row['fill_color'], 
			color=row['color'], 
			fill_opacity = row['fill_opacity']
		).add_to(marker_cluster)
	# draw a line between the points	
	for i in range(len(df)-1):
		folium.PolyLine(
			[[df.iloc[i].lat,df.iloc[i].lon],[df.iloc[i+1].lat,df.iloc[i+1].lon]],
			weight=5,
			color='blue',
			opacity=0.5
		).add_to(map)
	return map._repr_html_()


async def call_map(request):
	logger.info("call_map")
	csv_text = str(await request.text()).replace('\ufeff', '')
	df = pd.read_csv(StringIO(csv_text), sep=';')
	logger.info('df len: '+str(len(df)))
	response = map_generator(df)
	logger.info("response len: "+str(len(response)))
	return web.Response(text=str(response),content_type="text/html")

app = web.Application(client_max_size=1024**3)
app.router.add_route('GET', '/test', call_test)
app.router.add_post('/map', call_map)

web.run_app(
    app,
    port=os.environ.get('PORT', ''),
)
