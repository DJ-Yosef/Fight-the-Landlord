import random
import sys

rank = [str(i)for i in range(3,11)] + list("JQKA2小大")
color = {'♠':3, '♥':2, '◆':1, '♣':0}
total = [i+j for j in rank[:-2] for i in color] + ["0小","0大"]
color["0"] = 100


def card_sort(t):
    return rank.index(t[1:]),color[t[0]]


def squence(s,way=0):
    n = len(s)
    if (n < 5 or rank.index(s[-1])>rank.index("A")):
        return None
    if len(set(s)) == n:
        for i in range(1,n):
            if rank.index(s[i]) - rank.index(s[i-1]) != 1:
                break
        if i == n-1:
            return (f"顺子（{s[0]}-{s[-1]}）|{n}张",1,
                    ( n,rank.index(s[0]) ) )[way]
    
    if (n%2 != 0 or len(set(s))*2 != n or s[0] != s[1]):
        return None
    for i in range(2,n,2):
        if not(s[i] == s[i+1] and
               rank.index(s[i]) - rank.index(s[i-2]) == 1):
            break
    if i == n-2:
        return (f"连对（{s[0]}-{s[-1]}）|{n}张",2,
                ( n,rank.index(s[0]) ) )[way]
    
def judge(s,way=0):
    s.sort(key=card_sort)
    s = [i[1:] for i in s]
    n = len(s)
    if n >= 5:
        ans = squence(s,way)
        if ans:return ans

    if n == 1:
        return (random.choice([f"单牌（{s[0]}）",f"单走一张{s[0]}"]),3,
                rank.index(s[0]) )[way]
    elif n == 2:
        if s[0] == s[1]:
            return (random.choice([f"对子（{s[0]}）",f"对{s[0]}"]),4,
                    rank.index(s[0]) )[way]
    elif n == 4:
        if len(set(s)) not in [1,2]:
            return None
        if s[0] != s[3]:
            if s[0] == s[1]:t = s[0]
            else:t = s[1]
            return (random.choice([f"三带一（{t}）",f"三飘一（{t}）"]),5,
                    rank.index(s[0]) )[way]
        return (random.choice([f"炸了！（{s[0]}）",f"{s[0]}炸！"]),6,
                rank.index(s[0]) )[way]
    elif n == 5:
        if not 2<=len(set(s))<=3:
            return None
        t = s[2]
        if (s[0] == s[2]):
            if (s[3] == s[4]):
                return (f"三带一对儿（{s[0]}）",7,
                        rank.index(s[0]))[way]
            return (f"三带二（{s[0]}）",8,
                    rank.index(s[0]) )[way]
        elif (s[4] == s[2]):
            if (s[0] == s[1]):
                return (f"三带一对儿（{s[0]}）",7,
                        rank.index(s[0]))[way]
            return (f"三带二（{s[0]}）",8,
                    rank.index(s[0]) )[way]
        else:
            return (f"三带二（{s[0]}）",8,
                    rank.index(s[0]) )[way]
            
    elif n == 6:
        if s[2] == s[3]:
            t = s[3]
            if (s[0] == s[1] == s[2]):
                if (s[4] == s[5]):
                    return (f"四带一对（{t}）",9,
                            rank.index(t) )[way]
                return (f"四带二（{t}）",10,
                        rank.index(t) )[way]
            elif (s[3] == s[4] == s[5]):
                if (s[0] == s[1]):
                    return (f"四带一对（{t}）",9,
                            rank.index(t) )[way]
                return (f"四带二（{t}）",10,
                        rank.index(t) )[way]
        elif ((s[0] == s[1] == s[2])and
              (s[3] == s[4] == s[5])):
            return (f"{s[0]}|{s[3]} 飞机",11,
                    rank.index(s[0]) )[way]
    elif n == 8:
        if ((s[0] == s[1] == s[2])and
            (s[3] == s[4] == s[5])and
            (s[0] not in [s[6],s[7]])and
            (s[3] not in [s[6],s[7]])):
            return (f"{s[0]}|{s[3]} 飞机带翅膀 {s[6]}&{s[7]}",12,
                    rank.index(s[0]) )[way]
        elif ((s[2] == s[3] == s[4])and
            (s[5] == s[6] == s[7])and
            (s[2] not in [s[0],s[1]])and
            (s[5] not in [s[0],s[1]])):
            return (f"{s[2]}|{s[5]} 飞机带翅膀 {s[0]}&{s[1]}",12,
                    rank.index(s[0]) )[way]
        elif ((s[0] == s[1] == s[2])and
            (s[5] == s[6] == s[7])and
            (s[0] not in [s[3],s[4]])and
            (s[5] not in [s[3],s[4]])):
            return (f"{s[0]}|{s[5]} 飞机带翅膀 {s[3]}&{s[4]}",12,
                    rank.index(s[0]) )[way]
##        elif:
##            ...
##        elif:
##            ...

        


def fight(decision,last,passcnt):
    if (passcnt == 2) or (not last):return True  # 场上第一次出牌
    
    d = judge(decision,1)
    la = judge(last,1)
    if d != la and d != 6:return -1  # 非同类型or炸弹
    if d == 6 and la != 6:return True  # decision炸弹
    if d == la:
        if (d in [1,2]) and (len(decision) != len(last)):return -1
        # 同为顺子但长度不同
        d = judge(decision,2)
        la = judge(last,2)
        if d > la:
            return True
        return False
        
        

