import random
for cardfunction import *
class player:
    '''游戏玩家'''
    num=1
    def __init__(self,name=f"玩家{player.num}"):
        player.num += 1
        self.name = name
        self.card=[]
        print(f"{name} 创建成功！")
    def rename(self,newname=""):
        if newname:
            print(f"{self.name} 重命名为 {newname}")
            self.name=newname

def deal():
    '''发牌'''
    rank = [str(i)for i in range(3,11)] + list("JQKA2小大")
    color = {'♠':3, '♥':2, '◆':1, '♣':0}
    total = [i+j for j in rank[:-2] for i in color] + ["0小","0大"]
    color["0"] = 100

    random.shuffle(total)  # 洗牌

    for i in range(17):  # 发牌
        pler_a.append(total.pop())
        pler_b.append(total.pop())
        pler_c.append(total.pop())

    pler_a.sort(key=card_sort)  # 理牌
    pler_b.sort(key=card_sort)
    pler_c.sort(key=card_sort)
    luck = random.choice(player_list)  # 地主
    eval(f"player_{luck}").extend(total)
    eval(f"player_{luck}").sort(key=card_sort)
    print(f"player_{luck} is the Field Owner!\n")
    print("地主牌：",total)
    return

def main():
    #生成玩家
    for i in (1,2,3):
        name = input(f"请玩家{i}命名自己的角色\n（默认名玩家{i}）：")
        exec(f"pler_{96+i}=player(name)")
    #发牌
    deal()
