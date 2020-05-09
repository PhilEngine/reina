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

def get_h_image(data):
    post_packet = {
        "toUser": data['FromGroupId'],
        "sendToType": 2,
        "sendMsgType": "PicMsg",
        "content": "给",
        "picUrl": 'https://uploadbeta.com/api/pictures/random/?key=%E6%8E%A8%E5%A5%B3%E9%83%8E',
        "groupid": 0,
        "atUser": 0,
        "picBase64Buf": '',
        "fileMd5": '',
        "replayInfo": "null"
    }
    return post_packet

def get_random_image(data):
    post_packet = {
        "toUser": data['FromGroupId'],
        "sendToType": 2,
        "sendMsgType": "PicMsg",
        "content": "给",
        "picUrl": 'https://img.xjh.me/random_img.php',
        "groupid": 0,
        "atUser": 0,
        "picBase64Buf": '',
        "fileMd5": '',
        "replayInfo": "null"
    }
    return post_packet
    