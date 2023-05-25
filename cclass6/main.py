import webapp2
class MainPage(webapp2.RequestHandler) :
    def get(self) :
        i=1
        f0=0
        f1=1
        while(i<8) :
            self.response.out.write(f0)
            self.response.out.write("\n")
            f1=f0+f1
            f0=f1-f0
            i=i+1
app=webapp2.WSGIApplication([('/',MainPage)],debug=True)
