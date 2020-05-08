
## 解析群消息，参数 data 为 dict 字典，格式例如下：
#{
#   'FromGroupId': 111111111,     ## 消息来自的群号
#   'FromGroupName': '哲学开源',   ## 消息来自的群名  
#   'FromUserId': 222222222,      ## 发消息的群友Q号
#   'FromNickName': '一直女装',    ## 发消息的群友名称 
#   'Content': 'test test',       ## 消息内容 
#   'MsgType': 'TextMsg',         ## 消息类型
#   'MsgTime': 1588936934,        ## 消息时间
#   'MsgSeq': 9161,               ## 消息序列
#   'MsgRandom': 1702879550,      ## 消息随机数
#   'RedBaginfo': None            ## 其他包信息
#}
## 函数返回一个 dict 字典，格式例如下：
#{
#   "toUser":111111111,           ## 消息发送的群号
#   "sendToType":2,               ## 2，表示发到群里
#   "sendMsgType":"TextMsg",      ## 消息类型，暂时只考虑文本 TextMsg
#   "content":"I am here!",       ## 消息内容，需要根据收到的消息来解析
#   "groupid":0,                  ## 0
#   "atUser":0,                   ## @某个群友，暂时填0
#   "replayInfo":null             ## null
#}
def grp_msg_parse(data):
    ret = str()
    ## TODO

    return ret