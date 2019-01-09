import webapp2


# handlers
class MainHandler(webapp2.RequestHandler):
    def get(self):
        return self.response.write('Hello, SmartNinja!')


# URLs
app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)


# run on server
localhost = True  # True: non-GAE localhost server; False: GAE on either localhost or on Google Cloud
if localhost:
    def main():
        from paste import httpserver
        httpserver.serve(app, host='localhost', port='8080')


    if __name__ == '__main__':
        main()
