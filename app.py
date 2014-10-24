# mongo user amm-csr
# mongo password &Zt^7G7S


from pymongo import MongoClient

import tornado.ioloop
import tornado.web

def mongo():
    client = MongoClient('mongodb://{}:{}@ds043350.mongolab.com:43350/amm-test'.format('amm-csr',
                                                                                       '&Zt^7G7S'))
    
    db = client.get_default_database()
    

def root(tornado.web.RequestHandler):
    def get():
        self.render()

app = tornado.web.Application([
        (r'/', root)
    ])

if __name__=="__main__":
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()