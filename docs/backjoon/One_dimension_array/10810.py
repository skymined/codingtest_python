#https://www.acmicpc.net/problem/

# 문제
## 

#입력
## 첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.
## 둘째 줄부터 M개의 줄에 걸쳐서 공을 넣는 방법이 주어진다. 각 방법은 세 정수 i j k로 이루어져 있으며, i번 바구니부터 j번 바구니까지에 k번 번호가 적혀져 있는 공을 넣는다는 뜻이다.
## 예를 들어, 2 5 6은 2번 바구니부터 5번 바구니까지에 6번 공을 넣는다는 뜻이다. (1 ≤ i ≤ j ≤ N, 1 ≤ k ≤ N)
## 도현이는 입력으로 주어진 순서대로 공을 넣는다.

#출력
## 1번 바구니부터 N번 바구니에 들어있는 공의 번호를 공백으로 구분해 출력한다. 공이 들어있지 않은 바구니는 0을 출력한다.

N, M = map(int, input().split())
# N개의 바구니 N개의 공을 가지고 있고 M번 행동함
box = []
for i in range(N) : 
    box.append(0)
pass
# box를 만들고 그 안에 N개의 바구니를 장착함
## 이거 그냥 box=[0]*N 으로 하면 된답니다....

for i in range(M):
    first, second, num = map(int, input().split()) # first와 second는 바구니의 범위, num은 거기 안에 넣는 공의 숫자를 의미함
    box[first-1:second]=[num]*(second-first+1)
print(*box, end="")

