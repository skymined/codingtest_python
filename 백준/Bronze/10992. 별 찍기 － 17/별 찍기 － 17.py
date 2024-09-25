n = int(input())

for i in range(1,n):
    if i == 1:
        print(" "*(n-i)+"*")
    else :
        print(" "*(n-i)+"*", end="")
        print(" "*(2*(i)-3)+"*")
print("*"*(2*n-1))
