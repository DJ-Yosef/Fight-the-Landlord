import random
import sys
from card_functions import *
rank = [str(i)for i in range(3,11)] + list("JQKA2小大")
color = {'♠':3, '♥':2, '◆':1, '♣':0}
total = [i+j for j in rank[:-2] for i in color] + ["0小","0大"]
color["0"] = 100

player_list = "abc"
player_a = []
player_b = []
player_c = []
history = []

random.shuffle(total)  # 洗牌
for i in range(17):  # 发牌
    player_a.append(total.pop())
    player_b.append(total.pop())
    player_c.append(total.pop())

player_a.sort(key=card_sort)  # 理牌
player_b.sort(key=card_sort)
player_c.sort(key=card_sort)

print("地主牌：",total)
luck = random.choice(player_list)  # 地主
eval(f"player_{luck}").extend(total)
eval(f"player_{luck}").sort(key=card_sort)
print(f"player_{luck} is the Field Owner!\n")
print("Game Begin!\n")

last = []
temp = []
cur = player_list.index(luck)
##sys.exit()
passcnt = 0
flag1 = True  # 是否处于同一玩家操作阶段

while (player_a and player_b and player_c):
    if flag1:
        hand = eval(f"player_{player_list[cur]}")
        print(f"该 player_{player_list[cur]} 出牌了"
              "（您的手牌为：）")
        print(" ".join(hand))
        print("输入您的牌面，以空格分割"
              "（回车跳过回合）"
              "\n输入'h'查看历史出牌：")
    temp = [i[1:] for i in hand]
    decision = []
    choice = input().upper()
    if not choice:
        choice = input("是否跳过？再次回车跳过，继续出牌请输入牌面："
                       "\n输入'h'查看历史出牌：")
        if not choice:
            print( f"player_{player_list[cur]}：",
                   random.choice(["过","pass","要不起"])+"\n" )
            passcnt = (passcnt-1)%2+2
            flag1 = True
            cur = (cur+1)%3
            continue
        elif choice == "H":
            if not history:print("无历史出牌")
            for i in range(len(history)):
                print(history[i],end="  ")
                if i %2 == 1 or i == len(history)-1:print()
            flag1 = False
            continue
    elif choice == "H":
        if not history:print("无历史出牌")
        for i in range(len(history)):
            print(history[i],end="  ")
            if i %2 == 1 or len(history) == 1:print()
        flag1 = False
        continue
    try:
        choice = choice.split()
##        choice = list(map(lambda x:int(x)-1,choice.split()))
        for i in range(len(choice)):
            decision.append(temp.index(choice[i]))
            temp[decision[i]] = None
        ds2 = decision.copy()
        decision = [hand[i] for i in decision]
##    except IndexError:
    except ValueError:
        print("出牌错误，请检查牌面！")
        flag1 = False
        continue
    print("请确认您的选择：\n",decision,"输入0重选，其他内容确认")
    rechose = input()
    if rechose == "0":
        flag1 = False
        print("请重选：")
        continue
    result = judge(decision,0)
    if not result:
        print("出牌错误，请正确出牌！")
        flag1 = False
        continue
    
    # 比较大小 未实现
    if fight(decision,last,passcnt) == -1:
        print("请选择同种牌面or炸弹")
        flag1 = False
        continue
    elif not fight(decision,last,passcnt):
        print(f"换一副吧，管不了！")
        flag1 = False
        continue
    passcnt = 0
    history.append( (f"player_{player_list[cur]}:",result) )
    print(f"player_{player_list[cur]}:",result,
          f"{random.choice(['管上',''])}\n")
##    print(decision,"\n",hand,"\n\n\n")
    for i in decision:
        hand.remove(i)
    if cur == 0:
        player_a = list(hand)
    elif cur == 1:
        b = list(hand)
    else:
        c = list(hand)
##    hand_change(player_list[cur],hand,player_a,player_b,player_c)
    # 改变手牌
##    eval(f"player_{player_list[cur]}") = list(hand.values())
##    不能对eval对象赋值
##    print("您的手牌现在为",eval(f"player_{player_list[cur]}"))
    last = decision
    cur = (cur+1)%3
    flag1 = True

else:
    if not eval(f"player_{luck}"):
        print( random.choice(["地主胜利!","地主的春天！~"]) )
    else:
        print( random.choice(["农民翻身啦！","农民胜利！"]) )







