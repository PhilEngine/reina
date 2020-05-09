import urllib.request as urllib2
from io import StringIO
from PIL import Image
import base64

def get_img_base64_from_url(url):
    try:
        origin_file = StringIO.StringIO(urllib2.urlopen(url).read())
        img = Image.open(origin_file)
        jpeg_image_buffer = StringIO.StringIO()
        img.save(jpeg_image_buffer, format="JPEG")
        base64_str = base64.b64encode(jpeg_image_buffer.getvalue())
        return base64_str
    except:
        return None
