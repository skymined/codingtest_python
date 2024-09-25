n = int(input())

for i in range(1,n+1):
    print("*"*i+" "*(2*n-2*i)+"*"*i)
for i in range(1,n):
    print("*"*(n-i)+" "*(2*i)+"*"*(n-i))



# 1 8 1
# 2 6 2
# 3 4 3
# 4 2 4
# 5 0 5
# 4 2 4