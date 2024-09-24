##>>> hand = ['♣4', '◆4', '♥5', '♠5', '◆6', '♥6', '♠6',
##            '♣7', '◆8', '♠8', '♣9', '◆9', '♠10', '◆Q',
##            '♥Q', '♥K', '♠K', '♣A']
##>>> decision = ['♣4', '◆4']
##>>> hand = list(map(lambda x:x not in decision,hand))
##>>> hand
##[False, False, True, True, True, True,
## True, True, True, True, True, True, True,
## True, True, True, True, True]

##def hand_change(decision,hand):
##    for i



##for i in range(...,n,2):
##TypeError: 'ellipsis' object cannot be interpreted as an integer
## ['♣6', '♥6', '♠6', '♠5'] 1确认，0重选
##1
##出牌错误，请正确出牌！
##该 player_c 出牌了（您的手牌为：）


##    t = [[f"单牌（{s[0]}）",f"单走一张{s[0]}"],
##         [f"对子（{s[0]}）",f"对{s[0]}"],
##         f"三带一（{s[0]}）",
##         [f"炸了！（{s[0]}）",f"{s[0]}炸！"],
##         f"三带一对儿（{s[0]}）",
##         f"三带二（{s[0]}）",
##         f"四带一对（{s[0]}）",
##         ]
##    style = {i:t[i] for i in range(len(t))}

##    hand_change(player_list[cur],hand,player_a,player_b,player_c)
    # 改变手牌
##    eval(f"player_{player_list[cur]}") = list(hand.values())
##    不能对eval对象赋值
##    print("您的手牌现在为",eval(f"player_{player_list[cur]}"))

    
