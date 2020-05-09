import urllib2
import cStringIO
from PIL import Image
import base64

def get_img_base64_from_url(url):
    try:
        origin_file = cStringIO.StringIO(urllib2.urlopen(url).read())
        img = Image.open(origin_file)
        jpeg_image_buffer = cStringIO.StringIO()
        img.save(jpeg_image_buffer, format="JPEG")
        base64_str = base64.b64encode(jpeg_image_buffer.getvalue())
        return base64_str
    except Exception, e:
        return None