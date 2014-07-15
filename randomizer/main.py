import tornado
import importlib
from motorengine.connection import connect

from randomizer import routes


def run(settings_module):
    """
    Run the app using specified settings
    """
    settings = importlib.import_module(settings_module)
    app = tornado.web.Application(routes.urls, **settings.TORNADO)
    app.listen(settings.TORNADO['port'], '127.0.0.1')

    io_loop = tornado.ioloop.IOLoop.instance()

    connect(settings.MONGO['name'], io_loop=io_loop,
            **settings.MONGO['options'])

    io_loop.start()
