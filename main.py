import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

tornado.options.define(
    "port",
    default=5000,
    help="run on the given port",
    type=int,
)



class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r'/', HomeHandler),
            (r'/yaml', YAMLHandler),
            (r'/queue', QueueHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=False,
        )
        tornado.web.Application.__init__(self, handlers, **settings)


class HomeHandler(tornado.web.RequestHandler):

    def get(self):
        self.render(
            "home.html",
        )


class YAMLHandler(tornado.web.RequestHandler):

    def get(self):
        self.render(
            "yaml.html",
        )


class QueueHandler(tornado.web.RequestHandler):

    def get(self):
        self.render(
            "queue.html",
        )


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(tornado.options.options.port)

    print 'Server started 127.0.0.1:5000'
    print 'Control-C to quit'

    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
