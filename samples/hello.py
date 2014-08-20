from sola.web import WebServer


class HelloRoot(object):

	def index(self, page='Index'):
		return 'Current page is %s' % (page)

	def page(self, page):
		return page

class HelloWebserver(WebServer):

	def create_app(self):
		ctl = HelloRoot()
		route = self.new_route()
		route.mapper.explicit = False
		route.connect('index', '/', controller=ctl, action='index')
		route.connect('page', '/page/:page', controller=ctl, action='page')
		return ctl, route


if __name__ == '__main__':
	HelloWebserver().serve_forever()
