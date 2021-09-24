from aiohttp import web
import os
#import json
import folium
from folium.plugins import MarkerCluster
import pandas as pd
from io import StringIO

async def call_test(request):
	content = "get ok"
	return web.Response(text=content,content_type="text/html")

async def call_map(request):
	
	csv_text = str(await request.text()).replace('\ufeff', '')
	#print(csv_text)
	df = pd.read_csv(StringIO(csv_text), sep=';')
	print(df)
	#request_str = json.loads(request_str)
	#request = json.loads(request_str)
	#print(request)
	response = 'post ok\n'+str(df)
	return web.Response(text=str(response),content_type="text/html")

app = web.Application(client_max_size=1024**3)
app.router.add_route('GET', '/test', call_test)
app.router.add_post('/map', call_map)

web.run_app(
    app,
    port=os.environ.get('PORT', ''),
)
