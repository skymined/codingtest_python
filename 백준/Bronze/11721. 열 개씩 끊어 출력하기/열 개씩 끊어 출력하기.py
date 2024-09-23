import sys

data = sys.stdin.readline().rstrip()
a = len(data) // 10

for i in range(a+1) :
    print(data[10*i: 10*(i+1)])