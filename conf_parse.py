import configparser
import os

class Conf:
    def __init__(self):
        if not os.path.exists("reina.conf"):
            print("Config reina.conf not exists!")
            with open("reina.conf", "w") as f:
                f.write("[Reina]\n")
                f.write("REINA_QQ = \n")
                f.write("REINA_IP = \n")
            exit()

        cfg = configparser.ConfigParser()
        cfg.read("reina.conf")

        self.REINA_QQ = cfg["Reina"]["REINA_QQ"]
        self.REINA_IP = cfg["Reina"]["REINA_IP"]
        self.REINA_NAME_ZH_CN = ['爱奈', '艾乃', '爱乃', '艾奈']
        self.POST_URL = self.REINA_IP + '/v1/LuaApiCaller?qq=' \
            + self.REINA_QQ + '&funcname=SendMsg&timeout=10'        
    pass
