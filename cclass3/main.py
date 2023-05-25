import webapp2
class MainPage(webapp2.RequestHandler) :
    def get(self) :
        self.response.headers["Content-Type"]="text/plain"
        i=1
        while i < 10 :
            self.response.out.write("haripriya here 33328\n")
            i=i+1
app=webapp2.WSGIApplication([('/',MainPage)],debug=True)

