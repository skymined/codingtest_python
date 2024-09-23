#https://www.acmicpc.net/problem/2444

# 문제
## 

#입력
## 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

#출력
## 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.


N= int(input())

for i in range(1,N+1) : 
    print(' '*(N-i)+'*'*(2*i-1))
for j in range(1,N) :
    print(' '*j+'*'*(2*N-1-2*j))
