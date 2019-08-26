from importlib import reload
import io
import prozelLang

class request():
    
    def __init__(self, uri, data, method, remoteAddr):
        print("[REQUEST] Handling new Reqest...")
        self.data       = data
        self.method     = method
        self.remoteAddr = remoteAddr
        self.code       = 200 
        self.uri        = uri
        self.uri = uri.split("?", 1)

        print("[REQUEST] Processing Data:\nRemote: {}\nURI: {}\nMethod: {}".format(self.remoteAddr, self.uri, self.method))
    def responseCode(self):
        return self.code
    def headers(self):
        headersvalue = {}
        headers      = []
        headers.append("X-Prozel-Server")
        headersvalue["X-Prozel-Server"] = "0.1b"
        if self.uri[0].split(".")[-1] == "css":
            headers.append("Content-Type")
            headersvalue["Content-Type"] = "text/css"
        if self.uri[0].split(".")[-1] == "html":
            headers.append("Content-Type")
            headersvalue["Content-Type"] = "text/html"
        if self.uri[0].split(".")[-1] == "jpeg":
            headers.append("Content-Type")
            headersvalue["Content-Type"] = "image/jpeg"
        if self.uri[0].split(".")[-1] == "jpg":
            headers.append("Content-Type")
            headersvalue["Content-Type"] = "image/jpeg"
        if self.uri[0].split(".")[-1] == "jpe":
            headers.append("Content-Type")
            headersvalue["Content-Type"] = "image/jpeg"
        if self.uri[0].split(".")[-1] == "png":
            headers.append("Content-Type")
            headersvalue["Content-Type"] = "image/png"
        if self.uri[0].split(".")[-1] == "js":
            headers.append("Content-Type")
            headersvalue["Content-Type"] = "application/javascript"
        return (headers, headersvalue)

    def responseData(self):
        reload(prozelLang)
        if self.uri[0] == "/":
            self.uri[0] = "/index.html"
        try:
            with open("web{}".format(self.uri[0]),"r") as file:
                tmpResp = file.read().replace("\n", "")
                processedResp = prozelLang.Process(tmpResp)
        except FileNotFoundError:
            self.code = 404
            with open("error{}".format("/404.html"),"r") as file:
                tmpResp = file.read().replace("\n", "")
                processedResp = prozelLang.Process(tmpResp)
        return bytes(processedResp.get_string(), 'utf-8')