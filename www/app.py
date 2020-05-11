import logging; logging.basicConfig(level=logging.INFO)
import asyncio, os, time, json
from datetime import datetime
from aiohttp import web


async def index(request):
    return web.Response(body=b'<h1>wowwwwwww</h1>',content_type='text/html')


def init():
    app = web.Application()
    app.add_routes([web.get('/', index)])
    web.run_app(app, host='0.0.0.0', port=8080)
    logging.info('Server started at 127.0.0.1:8080')


init()
