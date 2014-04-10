import time
import cgi
import json
import os
import BaseHTTPServer

HOST_NAME = 'localhost'
PORT_NUMBER = 9300

class PlayerService(BaseHTTPServer.BaseHTTPRequestHandler):

    def do_POST(self):

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
        if ctype == 'multipart/form-data':
            postvars = cgi.parse_multipart(self.rfile, pdict)
        elif ctype == 'application/x-www-form-urlencoded':
            length = int(self.headers.getheader('content-length'))
            postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
        else:
            postvars = {}

        action = postvars['action'][0]

        w, r = os.popen2("./player " + action)

        if 'game_state' in postvars:
            game_state = postvars['game_state'][0]
            w.write(game_state)

        w.close()

        response = r.read()

        self.wfile.write(response)
    def log_message(self, format, *args):
        return


if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), PlayerService)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)
