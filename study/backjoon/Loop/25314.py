#https://www.acmicpc.net/problem/25304

# 문제
## Hello World!를 출력하시오.

#입력
## 첫 번째 줄에는 문제의 정수 N이 주어진다.(4<=N<=1000, N은 4의 배수)

#출력
## 헤아가 N바이트 정수까지 저장할 수 있다고 생각하는 정수 자료형의 이름을 출력하여라.

n=int(input())
num = int(n/4)

print("long "*num+"int")



