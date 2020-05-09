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

    def get_current_boss(self):
        boss_hpavail = self.boss[self.current_boss][0]
        boss_hpall = self.boss[self.current_boss][1]
        ret = str(self.syuume) + "周目，" + \
              str(self.current_boss) + "王\n" + \
              str(boss_hpavail) + "/" + \
              str(boss_hpall) + "，" + \
              str(round(boss_hpavail / boss_hpall * 100, 2)) + "%"
        return ret


class Member:
    def __init__(self):
        self.member = dict()
        self.member_mapping = dict()

        if not os.path.exists("member.csv"):
            print("Config member.csv not exists!")
            exit()
        with open("member.csv", "rt") as f:
            for line in f:
                nicks = line.strip().split(",")
                qq = int(nicks[0])
                self.member[qq] = {
                    'nick': nicks[1],
                    'short_nick': nicks[2],
                    'nr_cutter': 0,
                    0: {
                        'boss': 0,
                        'simulate': 0,
                        'actual': 0
                    },
                    1: {
                        'boss': 0,
                        'simulate': 0,
                        'actual': 0
                    },
                    2: {
                        'boss': 0,
                        'simulate': 0,
                        'actual': 0
                    },
                    3: {        ## 尾刀后的补偿刀
                        'boss': 0,
                        'simulate': 0,
                        'actual': 0
                    }
                }
                self.member_mapping[nicks[1]] = qq
            pass
        pass
    pass

    ## 统计对某个 boss 造成的伤害
    ## boss_id 为第几个 boss
    ## is_all_damaged 默认为 False，表示只统计指定的 boss
    ## 若将 is_all_damaged 设为 True，则表示统计今日的出刀情况
    def get_boss_damage(self, boss_id=0, is_all_damaged=False):
        damage_list = list()
        qqs = self.member.keys()
        for qq in qqs:
            nick = self.member[qq]['short_nick']
            nr_cutter = self.member[qq]['nr_cutter']
            sim_all = 0
            act_all = 0
            if nr_cutter == 0:
                continue

            for i in range(0, nr_cutter):
                
                elem = self.member[qq][i]
                if not is_all_damaged:
                    if elem["boss"] != boss_id:
                        continue
                sim_all += elem["simulate"]
                act_all += elem["actual"]
            damage_list.append([nick, nr_cutter, sim_all, act_all])
        damage_list = sorted(damage_list, key=lambda x:x[3], reverse=True)

        ret = str()
        if len(damage_list) == 0:
            return "今日尚无出刀统计"
        for i in damage_list:
            ret += i[0] + "，" + str(i[1]) + "刀" + \
                   str(act_all // 1000) + "w" + "，模拟：" + \
                   str(sim_all // 1000) + "w\n"
        return ret

    ## 统计未出刀的情况
    def get_not_cutted(self):
        damage_list = list()
        qqs = self.member.keys()
        for qq in qqs:
            nick = self.member[qq]['short_nick']
            nr_cutter = self.member[qq]['nr_cutter']
            if nr_cutter < 3:
                damage_list.append([nick, 3 - nr_cutter])
           
        damage_list = sorted(damage_list, key=lambda x:x[1], reverse=True)

        ret = str()
        c = 0
        if len(damage_list) == 0:
            return "今日已全部出完"
        for i in damage_list:
            ret += i[0] + "(" + str(i[1]) + "刀)  "
            c += 1
            if c / 2 == 0:
                ret += "\n"
        return ret

