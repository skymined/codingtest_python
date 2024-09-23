#https://www.acmicpc.net/problem/

# 문제
## 

#입력
## 첫째 줄에 알파벳 대문자로 이루어진 단어가 주어진다. 단어의 길이는 2보다 크거나 같고, 15보다 작거나 같다.

#출력
## 첫째 줄에 다이얼을 걸기 위해서 필요한 최소 시간을 출력한다.


# 문자와 숫자를 연동시켜두기

dic = {"A":2, "B":2, "C":2, "D":3, "E":3, "F":3, "G":4, "H":4, "I":4, "J":5, "K":5, "L":5, "M":6, "N":6, "O":6, "P":7, "Q":7, "R":7, "S":7, "T":8, "U":8,
       "V":8, "W":9, "X":9, "Y":9, "Z":9 }

input_data = list(input())
time_list=[]

for i in range(len(input_data)) :
    time_list.append(int(dic[input_data[i]])+1)

print(sum(time_list))
