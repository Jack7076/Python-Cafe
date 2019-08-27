from http.server import HTTPServer, BaseHTTPRequestHandler
from importlib import reload
import requestResponse
import prozelLang
import sys
import traceback

HTTP_PORT = 8000
LISTEN_ADDRESS = ""

class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.server_version = "Prozel Cloud Solutions High Performance HTTPD"
        self.sys_version = ""
        try:
            reload(requestResponse)
            resp = requestResponse.request(self.path, self.headers, self.command, self.address_string())
            respwrite = resp.responseData()
            self.send_response(resp.responseCode())
            hlist, hvalues = resp.headers()
            for header in hlist:
                self.send_header(header, hvalues[header])
                print("[HTTPD] Responding Header: {}: {}".format(header, hvalues[header]))
            self.end_headers()
            self.wfile.write(respwrite)
        except:
            print("[ERROR] Handling Error.")
            traceback.print_exc()
            self.send_response(500)
            self.end_headers()
            with open("error{}".format("/500.html"),"r") as file:
                tmpResp = file.read().replace("\n", "")
                processedResp = prozelLang.Process(tmpResp)
            self.wfile.write(bytes(processedResp.get_string(), 'utf-8'))
    def do_POST(self):
        self.server_version = "Prozel Cloud Solutions High Performance HTTPD"
        self.sys_version = ""
        try:
            reload(requestResponse)
            resp = requestResponse.request(self.path, self.headers, self.command, self.address_string())
            respwrite = resp.responseData()
            self.send_response(resp.responseCode())
            hlist, hvalues = resp.headers()
            for header in hlist:
                self.send_header(header, hvalues[header])
                print("[HTTPD] Responding Header: {}: {}".format(header, hvalues[header]))
            self.end_headers()
            self.wfile.write(respwrite)
        except:
            print("[ERROR] Handling Error.")
            traceback.print_exc()
            self.send_response(500)
            self.end_headers()
            with open("error{}".format("/500.html"),"r") as file:
                tmpResp = file.read().replace("\n", "")
                processedResp = prozelLang.Process(tmpResp)
            self.wfile.write(bytes(processedResp.get_string(), 'utf-8'))
        
httpd = HTTPServer((LISTEN_ADDRESS, HTTP_PORT), HTTPRequestHandler)
print(httpd.server_name)
try:
    print("[HTTPD] Starting HTTP Server")
    httpd.serve_forever()
except KeyboardInterrupt:
    print("[USER] CTRL + C Detected. Exiting...")
    sys.exit(10)
