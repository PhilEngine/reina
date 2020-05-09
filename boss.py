import os

class Boss:
    def __init__(self):
        self.boss = {
            1: [6000000, 6000000],
            2: [8000000, 8000000],
            3: [1000000, 1000000],
            4: [12000000, 12000000],
            5: [20000000, 20000000]
        }
        self.syuume = 1
        self.current_boss = 1
        self.queue = list()
    pass

    ## Boss 余血查询
    def get_current_boss(self):
        boss_hpavail = self.boss[self.current_boss][0]
        boss_hpall = self.boss[self.current_boss][1]
        ret = str(self.syuume) + "周目，" + \
              str(self.current_boss) + "王，余血：" + \
              str(round(boss_hpavail / boss_hpall * 100, 2)) + "%\n" + \
              str(boss_hpavail) + "/" + str(boss_hpall)
        return ret

    ## 查看当前队列
    def get_queue(self):
        ret = self.get_current_boss() + "\n"
        first_flag = True
        for i in self.queue:
            if first_flag:
                first_flag = False
                ret += i[1] + "，模拟刀：" + str(i[2] // 10000) + "w(作业中)\n"
                continue
            ret += i[1] + "，模拟刀：" + str(i[2] // 10000) + "w\n"
        return ret

    ## 排入新的刀
    def push_queue(self, qq, nick, simulate):
        self.queue.append(qq, nick, simulate)
        ret = "已排队，顺序如下：\n"
        first_flag = True
        for i in self.queue:
            if first_flag:
                first_flag = False
                ret += i[1] + "，模拟刀：" + str(i[2] // 10000) + "w(作业中)\n"
                continue
            ret += i[1] + "，模拟刀：" + str(i[2] // 10000) + "w\n"
        return ret

    ## 返回提示信息和上一刀的模拟伤害情况
    def pop_queue(self, qq, damage):
        self.boss[self.current_boss][0] -= min(self.boss[self.current_boss][0], damage)
        simulate = 0
        for i in range(0, len(self.queue)):
            if self.queue[i][0] == qq:
                simulate = self.queue[i][2]
                del self.queue[i]
        ret = str()
        if len(self.queue) > 0:
            ret = "请 " + self.queue[0][1] + " 出刀"
        else:
            ret = "无排队"
        return ret, simulate
