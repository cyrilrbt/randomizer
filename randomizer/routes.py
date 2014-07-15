from tornado.web import URLSpec as r
from randomizer.urler.handlers import URLerHandler, ShowHandler, RedirectHandler

urls = (
    # randomizer.urler
    r(r'/', URLerHandler, name='urler_new'),
    r(r'/link/(.*)', ShowHandler, name='urler_show'),
    r(r'/(.*)', RedirectHandler, name='urler_redirect'),
)
