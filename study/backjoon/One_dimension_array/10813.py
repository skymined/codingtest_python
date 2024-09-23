#https://www.acmicpc.net/problem/

# 문제
## 

#입력
## 첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.
# 둘째 줄부터 M개의 줄에 걸쳐서 공을 교환할 방법이 주어진다. 각 방법은 두 정수 i j로 이루어져 있으며, i번 바구니와 j번 바구니에 들어있는 공을 교환한다는 뜻이다. (1 ≤ i ≤ j ≤ N)
# 도현이는 입력으로 주어진 순서대로 공을 교환한다.

#출력
## 1번 바구니부터 N번 바구니에 들어있는 공의 번호를 공백으로 구분해 출력한다.

N, M = map(int, input().split())
# N개의 바구니와 N개의 공, 그리고 M번의 시도

box=list((range(1,N+1)))

for i in range(M) : 
    a, b = map(int, input().split())
    origin_1 = box[a-1] #a번 째에 있는 숫자 저장
    origin_2 = box[b-1] #b번 째에 있는 숫자 저장
    box[a-1]= origin_2
    box[b-1]= origin_1
    
print(*box, end="")


