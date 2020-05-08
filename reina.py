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

@sio.on('OnEvents')
def OnEvents(message):
    print(message)   

# ----------------------------------------------------- 
if __name__ == '__main__':
    sio.connect(robotip, transports=['websocket'])
    print("Start")
    sio.wait()
    sio.disconnect()
