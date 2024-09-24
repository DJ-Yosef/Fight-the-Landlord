import random
for cardfunction import *

"""在纸牌游戏中，需要一整副牌（a deck of cards），
而一摞牌叫stack，一个玩家（player）手上的牌叫一手（hand）牌。
纸牌正面（face/front）有不同的数字或字母和图案（motif），
背面（back）相同。在随机洗牌（randomized shuffling）时，
可以正面朝上（face up），也可以正面朝下（face down）。
给每个玩家分配纸牌时，叫发牌（deal）。发牌的人叫dealer，
banker是庄家，切牌叫cut the deck，开扇叫fan，摊牌用spread，
pass是移牌，force迫牌，riffle拨牌，bottom deal发底牌，
central deal发中间牌，palm是藏牌，top palm藏顶牌，
to stake下赌注，to raise加赌注，chip是筹码，in跟牌下注，
out不跟，to bid叫牌，犯规是infraction/break the rules。
"""

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
