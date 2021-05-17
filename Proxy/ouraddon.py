"""
unfinished version of the final addon : we could not finish it because of a compatibility problem with the pillow library

Run as follows: mitmdump -s ouraddon.py
"""
from mitmproxy import ctx
from mitmproxy import http
import Pillow
import io



class FindImages:
    def __init__(self):
        ctx.log.info("Starting...")

    def response(self, flow):
        if flow.response.headers.get("content-type", "").startswith("image"):
            image_data = flow.response.content
            img = Image.open(io.BytesIO(image_data))
            img.show()
            #img = img.save("image.jgp")


addons = [
    FindImages()
]
