import webapp2
class MainPage(webapp2.RequestHandler) :
    def get(self) :
        self.response.headers["Content-Type"]="text-plain"
        for i in range(5):
            self.response.out.write("i am haripriya and my seat number is 28 \n")
app=webapp2.WSGIApplication([('/',MainPage)],debug=True)