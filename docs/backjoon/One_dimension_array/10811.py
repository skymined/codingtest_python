#https://www.acmicpc.net/problem/10811

# 문제
## 

#입력
## 첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.
## 둘째 줄부터 M개의 줄에는 바구니의 순서를 역순으로 만드는 방법이 주어진다.
## 방법은 i j로 나타내고, 왼쪽으로부터 i번째 바구니부터 j번째 바구니의 순서를 역순으로 만든다는 뜻이다. 
## (1 ≤ i ≤ j ≤ N)
## 도현이는 입력으로 주어진 순서대로 바구니의 순서를 바꾼다.

#출력
## 모든 순서를 바꾼 다음에, 가장 왼쪽에 있는 바구니부터 바구니에 적혀있는 순서를 공백으로 구분해 출력한다.

N, M = map(int, input().split()) #N개의 바구니 #M번
list=list(range(1,N+1))
pass

for x in range(M) :
    a,b = map(int, input().split())
    if b-a <= 1 :
        list[a-1], list[b-1] = list[b-1], list[a-1]
        pass
    else : 
        for i in range((b-a+1)//2) :
            list[a-1+i], list[b-1-i] = list[b-1-i], list[a-1+i]
            pass

print(*list, end="")
    
