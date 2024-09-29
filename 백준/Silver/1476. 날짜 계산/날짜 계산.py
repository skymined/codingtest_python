E, S, M = map(int,input().split())
CNT = 1

# 1<=e<=15, 1<=s<=28, 1<=m<=19

while True :
    if (CNT-E) % 15 == 0 and (CNT-S) %28==0 and (CNT-M)%19==0:
        print(CNT)
        break
    CNT+=1