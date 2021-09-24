from aiohttp import web
import os
import json
import folium
from folium.plugins import MarkerCluster

async def call_test(request):
	content = "get ok"
	return web.Response(text=content,content_type="text/html")

async def call_map(request):
	
	request_str = str(await request.text()).replace('\ufeff', '')
	print(request_str)
	request_str = json.loads(request_str)
	request = json.loads(request_str)
	print(request)
	response = 'post ok\n'+str(request)
	return web.Response(text=str(response),content_type="text/html")

app = web.Application(client_max_size=1024**3)
app.router.add_route('GET', '/test', call_test)
app.router.add_post('/map', call_map)

web.run_app(
    app,
    port=os.environ.get('PORT', ''),
)
