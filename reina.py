import socketio
import requests
import json
import grp_msg_parse
import conf_parse
import extend

sio = socketio.Client()

# standard Python
#sio = socketio.Client(engineio_logger=True, logger=True)

# SocketIO Client
#sio = socketio.AsyncClient(logger=True, engineio_logger=True)

CONF = conf_parse.Conf()

# ----------------------------------------------------- 
@sio.event
def connect():
    print('Connected to Server')
    sio.emit('GetWebConn', CONF.REINA_QQ)

@sio.event
def disconnect():
    print('Disconnected')

## 接收群消息，参数 message 是一个 dict 结构，内容例如下：
#   {
#       'CurrentPacket': 
#       {
#           'WebConnId': '0PAeeBurA6MxKbLB2ELw', 
#           'Data': 
#           {
#               'FromGroupId': 111111111,     ## 消息来自的群号
#               'FromGroupName': '哲学开源',   ## 消息来自的群名  
#               'FromUserId': 222222222,      ## 发消息的群友Q号
#               'FromNickName': '一直女装',    ## 发消息的群友名称 
#               'Content': 'test test',       ## 消息内容 
#               'MsgType': 'TextMsg',         ## 消息类型
#               'MsgTime': 1588936934,        ## 消息时间
#               'MsgSeq': 9161,               ## 消息序列
#               'MsgRandom': 1702879550,      ## 消息随机数
#               'RedBaginfo': None            ## 其他包信息
#           }
#       }, 
#       'Current': 33333333                   ## 机器人Q号
#   }
@sio.on('OnGroupMsgs')
def OnGroupMsgs(message):
    data = message['CurrentPacket']['Data']
    content = data["Content"]
    if len(content) > 2 and content[:2] in CONF.REINA_NAME_ZH_CN:
        data["Content"] = content[2:].strip()
    if len(content) > 3 and content[:3].upper() == "ENE":
        data["Content"] = content[3:].strip()
    elif len(content) > 4 and content[:3].upper() == "@ENE":
        data["Content"] = content[3:].strip()
    elif len(content) > 5 and content[:3].upper() == "REINA":
        data["Content"] = content[3:].strip()
    elif len(content) > 6 and content[:3].upper() == "@REINA":
        data["Content"] = content[3:].strip()
    else:
        return 

    ret_packet = grp_msg_parse.grp_msg_parse(data)
    post_content = json.dumps(ret_packet)
    res = requests.post(url=CONF.POST_URL, data=post_content) 
    pass

## 接收好友消息，参数 message 是一个 dict 结构，内容例如下：
#   {
#       'CurrentPacket': 
#       {
#           'WebConnId': 'gq7eyyjpYanKRkzmvGQz', 
#           'Data': 
#           {   
#               'FromUin': 11111111,        ## 消息发送者Q号
#               'ToUin': 22222222,          ## 消息接收者Q号，即机器人Q号 
#               'MsgType': 'TextMsg',       ## 消息类型
#               'MsgSeq': 18110,            ## 消息序列
#               'Content': 'haha',          ## 消息内容
#               'RedBaginfo': None          ## 其他包信息
#           }
#       }, 
#       'CurrentQQ': 22222222               ## 机器人Q号
# }
@sio.on('OnFriendMsgs')
def OnFriendMsgs(message):
    data = message['CurrentPacket']['Data']
    content = data["Content"]
    if len(content) > 2 and content[:2] in CONF.REINA_NAME_ZH_CN:
        data["Content"] = content[2:].strip()
    if len(content) > 3 and content[:3].upper() == "ENE":
        data["Content"] = content[3:].strip()
    elif len(content) > 4 and content[:3].upper() == "@ENE":
        data["Content"] = content[3:].strip()
    elif len(content) > 5 and content[:3].upper() == "REINA":
        data["Content"] = content[3:].strip()
    elif len(content) > 6 and content[:3].upper() == "@REINA":
        data["Content"] = content[3:].strip()
    else:
        return 

    buf = extend.get_img_base64_from_url('https://uploadbeta.com/api/pictures/random/?key=%E6%8E%A8%E5%A5%B3%E9%83%8E')
    

    #ret_content = grp_msg_parse.grp_msg_parse(data)
    ret_content = ""
    post_packet = {
        "toUser": data["FromUin"],
        "sendToType": 1,
        "sendMsgType": "PicMsg",
        #"content": ret_content,
        "content": "拿去撸",
        "groupid": 0,
        "atUser": 0,
        "picBase64Buf": buf,
        "replayInfo": "null"
    }

    post_content = json.dumps(post_packet)
    res = requests.post(url=CONF.POST_URL, data=post_content) 
    pass

## 接收事件
@sio.on('OnEvents')
def OnEvents(message):
    ## print(message)   
    pass

# ----------------------------------------------------- 
if __name__ == '__main__':
    sio.connect(CONF.REINA_IP, transports=['websocket'])
    print("Reina Start")
    sio.wait()
    sio.disconnect()
