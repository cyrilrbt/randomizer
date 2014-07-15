import tornado


class Handler(tornado.web.RequestHandler):
    def absolute_url(self, name, *args, **kwargs):
        rc = "http://" + self.settings['domain_name']
        if self.settings.get('debug') and self.settings.get('port') \
           and self.settings.get('port') != 80:
            rc += ':' + str(self.settings['port'])
        try:
            rc += self.reverse_url(name, *args, **kwargs)
        except:
            rc += name
        return rc
