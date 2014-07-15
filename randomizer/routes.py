from tornado.web import URLSpec as r
from randomizer.urler.handlers import URLerHandler, RedirectHandler

urls = (
    # randomizer.urler
    r(r'/', URLerHandler, name='urler_new'),
    r(r'/(.*)', RedirectHandler, name='urler_redirect'),
)
