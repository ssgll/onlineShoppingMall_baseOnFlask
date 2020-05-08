# -*- coding: utf-8 -*-
from tornado.httpserver import HTTPServer
from tornado.wsgi import WSGIContainer
from manager import app
from tornado.ioloop import IOLoop
import platform

if platform.system() == "Windows":
    import asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


if __name__ == "__main__":
    server = HTTPServer(WSGIContainer(app))
    server.listen(5000)
    IOLoop.current().start()