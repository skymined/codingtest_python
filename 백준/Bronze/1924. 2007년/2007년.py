import sys

a,b = map(int, sys.stdin.readline().split())

if a ==1  :
    day = b
elif a ==2 :
    day = 31 +b
elif a<=8 and a > 2 : # 2~8월달일 떄
    if a % 2 == 0 : # 짝수일 때
        day = 61*(a//2-1) +31 + b -2
    else :
        day = 61*(a//2) + b -2
else :
    if a%2==0: # 짝수일 떄
        day = 245 + ((a-8)//2-1)*61 +30+b -2
    else :
        day = 245 + ((a-8)//2)*61 +b -2

t = day % 7

if t == 0 :
    print("SUN")
elif t ==1 :
    print("MON")
elif t ==2 :
    print("TUE")
elif t ==3 :
    print("WED")
elif t ==4 :
    print("THU")
elif t ==5 :
    print("FRI")
elif t ==6 :
    print("SAT")