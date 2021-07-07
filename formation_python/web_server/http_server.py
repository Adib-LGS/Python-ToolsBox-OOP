#Create own Basic Server o port 80
import http.server

class WebPageServer():

    port = 80
    #Host
    host_adress = ("", port)

    server = http.server.HTTPServer
    #Request Manager
    handler = http.server.CGIHTTPRequestHandler

    def __init__(self):
        pass

    @classmethod     
    def runServer(cls):
        #choose Protocol
        cls.handler.cgi_directories = ["//"]
        httpd = cls.server(cls.host_adress, cls.handler)
        print(f"Start Server using port: {cls.port}")
        httpd.serve_forever()