import socketio
import requests
import json

# standard Python
#sio = socketio.Client(engineio_logger=True, logger=True)
sio = socketio.Client()

# SocketIO Client
#sio = socketio.AsyncClient(logger=True, engineio_logger=True)

robotqq = ""
robotip = ""
posturl = robotip+'/v1/LuaApiCaller?qq='+robotqq+'&funcname=SendMsg&timeout=10'

# ----------------------------------------------------- 
@sio.event
def connect():
    print('connected to server')
    sio.emit('GetWebConn',robotqq)

@sio.event
def disconnect():
    print('disconnected')

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
    if content[:3] == "ene":
        postcont = '''{
            "toUser":908030069,
            "sendToType":2,
            "sendMsgType":"TextMsg",
            "content":"I am here!",
            "groupid":0,
            "atUser":0,
            "replayInfo":null
        }'''
    res = requests.post(url=posturl, data=postcont) 
    print(message)

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
    postcont = '''{
    "toUser":,
    "sendToType":1,
    "sendMsgType":"TextMsg",
    "content":"Hello",
    "groupid":0,
    "atUser":0,
    "replayInfo":null
    }'''
    res = requests.post(url=posturl, data=postcont)
    print(res.text)
    print(message)

## 接收事件
@sio.on('OnEvents')
def OnEvents(message):
    print(message)   

# ----------------------------------------------------- 
if __name__ == '__main__':
    sio.connect(robotip, transports=['websocket'])
    print("Start")
    sio.wait()
    sio.disconnect()
