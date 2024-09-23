#https://www.acmicpc.net/problem

# 문제
## (세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
##(1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.

#입력
## 첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.

#출력
## 첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한다.

### 1) 385 각 자리수 분리 2) 각 자리수와 (1)에 해당되는 값 곱셈 3) 각 자리에 10, 100을 곱한 후 더해서 (6)구하기

input_1= input()
input_2 = input()
input_2_new = list(map(int, str(input_2)))
a=int(input_1)*input_2_new[2]
b=int(input_1)*input_2_new[1]
c=int(input_1)*input_2_new[0]
d=a+10*b+100*c
print(a)
print(b)
print(c)
print(d)



