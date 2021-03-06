#!/usr/bin/env python3
import asyncio
from aiohttp import web
import urllib
import urllib.parse
from urllib.parse import urlparse, parse_qsl
import multidict as MultiDict
import requests
from map_gen import map_generator

async def load_map(request):
	request_id	= request.rel_url.query['request_id']
	content = "map not found"	
	with open("/home/alex/projects/map_server_folium/maps/"+request_id+".html","r") as file:
		content = file.read()
	return web.Response(text=content,content_type="text/html")
	

async def generate_map(request):
	request_id	= request.rel_url.query['request_id']
	lat	= request.rel_url.query['lat']
	lon	= request.rel_url.query['lon']
	zoom	= request.rel_url.query['zoom']
	show	= request.rel_url.query['show']
	#print("map_generator",request_id,lat,lon,zoom)
	content = map_generator(request_id,lat,lon,zoom,show)
	return web.Response(text=content,content_type="text/html")

app = web.Application()
app.router.add_route('GET', '/map', generate_map)
app.router.add_route('GET', '/load', load_map)

loop = asyncio.get_event_loop()
handler = app.make_handler()
f = loop.create_server(handler, port='8081')
srv = loop.run_until_complete(f)

print('serving on', srv.sockets[0].getsockname())
try:
	loop.run_forever()
except KeyboardInterrupt:
	print("serving off...")
finally:
	loop.run_until_complete(handler.finish_connections(1.0))
	srv.close()