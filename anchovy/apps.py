import tornado.web
import tornado.httpclient
from tornado.web import asynchronous
import tornado.gen as gen
import tornado.httpserver
import tornado.autoreload


import tornado.httpclient as httpclient
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.template
import tornado.gen

import time
import tornado.httpserver
import simplejson as json



class PretendService(tornado.web.RequestHandler):
	@asynchronous
  	def get(self):
  		""" Pretend some work is being done by sleeping for 500ms """
  		ioloop = tornado.ioloop.IOLoop.instance()
  		ioloop.add_timeout(time.time() + 0.5, self._finish_req)
 
 	def _finish_req(self):
 		#lf.finish({'someList': someList})
 		self.finish({'someList': 'helloFun'})


class MainHandlerAsync(tornado.web.RequestHandler):
	@asynchronous
	@gen.engine
	def get(self):
		req = httpclient.HTTPRequest(url='async', method='GET')
		client = tornado.httpclient.AsyncHTTPClient()
		# don't let the yield call confuse you, it's just Tornado helpers to make
		# writing async code a bit easier. This is the same as doing
		# client.fetch(req, callback=_some_other_helper_function)
		response = yield gen.Task(client.fetch, req)
		### do something with the response ###
		print dir(response)
		print '===== Body: ' 
		print dir(response.body)
		print '===== Headers: '
		print response.headers.items()
		self.finish({'someList': 'hello'})


 
if __name__ == "__main__":
	#define("port", default=8888, help="run on the given port", type=int)
	#tornado.options.parse_command_line()
	application = tornado.web.Application([
		(r"/async", MainHandlerAsync),
		(r"/external-api", PretendService)
		])
	http_server = tornado.httpserver.HTTPServer(application)
	http_server.listen(8888)
	tornado.autoreload.start()
	tornado.ioloop.IOLoop.instance().start()