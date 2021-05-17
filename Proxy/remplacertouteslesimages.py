"""
mitmproxy addon replacing all images with a locally saved image (must be in the same folder as the mitmproxy executables and named image.jpg)

Run as follows: mitmdump -s remplacertouteslesimages.py
"""
from mitmproxy import ctx
from mitmproxy import http



class FindImages:
    def __init__(self):
        ctx.log.info("Starting...")

    def response(self, flow):
        if flow.response.headers.get("content-type", "").startswith("image"):
            img = open("image.jpg", "rb").read()
            flow.response.content = img
            flow.response.headers["content-type"] = "image/jpg"
        


addons = [
    FindImages()
]
