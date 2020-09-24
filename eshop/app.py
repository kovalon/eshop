from aiohttp import web
from .routes import setup_routes
from aiohttp_swagger import *
import asyncpgsa


async def create_app():
    app = web.Application()
    setup_routes(app)
    setup_swagger(app, swagger_url="/api/v1/doc", ui_version=3)
    app.on_startup.append(on_start)
    app.on_cleanup.append(on_shutdown)
    return app


async def on_start(app):
    app['db'] = await asyncpgsa.create_pool(dsn='postgresql://postgres:postgres@localhost:5432/recurse')


async def on_shutdown(app):
    await app['db'].close()
