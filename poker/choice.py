import random
import sys
from card_functions import *
rank = [str(i)for i in range(3,11)] + list("JQKA2")
color = {'♠':3, '♥':2, '◆':1, '♣':0}
total = [i+j for j in rank for i in color]

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

print("地主牌：",total[0])
luck = random.choice(player_list)  # 地主
eval(f"player_{luck}").append(total.pop())
eval(f"player_{luck}").sort(key=card_sort)

cur = player_list.index(luck)
hand = eval(f"player_{player_list[cur]}")
print(hand)
temp = [i[1:] for i in hand]
decision = []
choice = input("请输入牌面：")
choice = choice.split()
try:
    for i in range(len(choice)):
        decision.append(temp.index(choice[i]))
        temp.pop(decision[i])
except ValueError:
    ...
    print("出牌错误，请检查出牌！")









##
##s = [ '♣'+str(i) for i in range(3,8)]*2
##s.sort()
##
##n = len(s)
##s = [i[1:] for i in s]
##if not n>=5:print( None);exit()
##for i in range(1,n):
##    if rank.index(s[i]) - rank.index(s[i-1]) != 1:
##        break
##if i == n-1:
##    print( f"顺子（{s[0]}-{s[-1]}）|{n}")
##if n%2 == 0:
##    if s[0] != s[1]:print(None);exit()
##    for i in range(2,n,2):
##        if not(s[i] == s[i+1] and
##               rank.index(s[i]) - rank.index(s[i-2]) == 1):
##            break
##    if i == n-2:
##        print( f"连对（{s[0]}-{s[-1]}）|{n}")
##
##
####for i in range(...,n,2):
####TypeError: 'ellipsis' object cannot be interpreted as an integer
