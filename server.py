#!/usr/bin/env python3
import asyncio
from aiohttp import web
import urllib
import urllib.parse
from urllib.parse import urlparse, parse_qsl
import multidict as MultiDict
import requests
from map_gen import map_generator

async def show_map(request):
	request_id	= request.rel_url.query['request_id']
	lat	= request.rel_url.query['lat']
	lon	= request.rel_url.query['lon']
	zoom	= request.rel_url.query['zoom']
	print("map_generator",request_id,lat,lon,zoom)
	content = map_generator(request_id,lat,lon,zoom)
	return web.Response(text=content,content_type="text/html")

app = web.Application()
app.router.add_route('GET', '/map', show_map)

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