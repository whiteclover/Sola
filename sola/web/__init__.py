import cherrypy
from sola.web.cherrye import patch_cherrypy

from gevent.wsgi import WSGIServer


class WebServer(object):

    def __init__(self, host='127.0.0.1', port=8080, encoding='utf-8'):
        self.httpd = None
        self.ready = False
        self.host = host
        self.port = port
        self.encoding = encoding

    def new_route(self):
        return cherrypy.dispatch.RoutesDispatcher()

    def create_app(self):
        raise NotImplemented('Must implement create_app in Subclass')

    def _start_app(self):
        ctl, routes = self.create_app()
        patch_cherrypy()
        conf = {
            'engine.autoreload.on': False,
            'log.screen': False,
            'log.error_file': '',
            'log.access_file': '',
            'environment': 'embedded',

            'tools.decode.on': unicode,
            'tools.encode.on': unicode,
            'tools.encode.encoding': self.encoding,
            'tools.gzip.on': True,
            'tools.log_headers.on': False,
            'request.show_tracebacks': False,
        }
        config = {'/': {'request.dispatch': routes}, 'global': conf}
        cherrypy.config.clear()
        cherrypy.config.update(config)
        app = cherrypy.tree.mount(ctl, '/', config)
        cherrypy.server.unsubscribe()

        self.httpd = WSGIServer((self.host, self.port), app)

    def serve_forever(self):
        self.ready = True
        self._start_app()
        cherrypy.engine.start()
        self.httpd.serve_forever()

    def stop(self):
        cherrypy.engine.stop()
        self.httpd.stop()
