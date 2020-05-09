import data_unit

GRP_MSG_PARSE_INIT_FLAG = True

BOSS = data_unit.Boss()
MEMBER = data_unit.Member()

def help():
    ret = '''ENE です，兰德索尔排刀助手
    (✪ω✪)
    1.boss/王
    2.出刀/申请出刀
    3.报刀/提交伤害
    4.队列
    5.已出刀
    6.未出刀
    7.统计
    8.修正/数据修正'''
    return ret

## 完成内容解析后，构造该结构用于发送到群里
def new_ret_dict(data):
    ret = { "toUser":data['FromGroupId'], 
            "sendToType":2,       
            "sendMsgType":"TextMsg",     
            "content":"",     
            "groupid":0,       
            "atUser":0,      
            "replayInfo":'null'
    }
    return ret

def grp_msg_parse_init():
    pass

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
    ## 程序重启后加载必要的数据
    global GRP_MSG_PARSE_INIT_FLAG
    global BOSS
    global MEMBER

    if GRP_MSG_PARSE_INIT_FLAG:
        GRP_MSG_PARSE_INIT_FLAG = False 
        grp_msg_parse_init()

    ret_content = str()
    content = data['Content']
    len_content = len(content)
    ## 帮助信息
    if len_content >= 2 and content[:2] in ['介绍', '帮助', '命令'] or \
            len_content >= 4 and content[:4].lower() == 'help' or \
            len_content >= 1 and content[0] == '?':
        ret_content = help()
    ## 获取 Boss 剩余血量
    elif len_content >= 1 and content[0] == '王' or \
            len_content >= 4 and content[:4].lower() == 'boss':
        ret_content = BOSS.get_current_boss()
    elif len_content >= 2 and content[:2] == '一王' or \
            len_content >= 2 and content[:2] == '1王':
        ret_content = MEMBER.get_boss_damage(boss_id=1)
    elif len_content >= 2 and content[:2] == '二王' or \
            len_content >= 2 and content[:2] == '2王':
        ret_content = MEMBER.get_boss_damage(boss_id=2)
    elif len_content >= 2 and content[:2] == '三王' or \
            len_content >= 2 and content[:2] == '3王':
        ret_content = MEMBER.get_boss_damage(boss_id=3)
    elif len_content >= 2 and content[:2] == '四王' or \
            len_content >= 2 and content[:2] == '4王':
        ret_content = MEMBER.get_boss_damage(boss_id=4)
    elif len_content >= 2 and content[:2] == '五王' or \
            len_content >= 2 and content[:2] == '5王':
        ret_content = MEMBER.get_boss_damage(boss_id=5)
    ## 已出刀统计
    elif len_content >= 3 and content[:3] == "已出刀":
        ret_content = MEMBER.get_boss_damage(boss_id=0, is_all_damaged=True)
    ## 未出刀统计
    elif len_content >= 3 and content[:3] == "未出刀":
        ret_content = MEMBER.get_not_cutted()

    ## TODO：解析消息并构造返回内容


    return ret_content
    # ret = new_ret_dict(data)
    # ret['content'] = ret_content
    # return ret
