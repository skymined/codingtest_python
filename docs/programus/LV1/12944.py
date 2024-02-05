# https://school.programmers.co.kr/learn/courses/30/lessons/12944
# 코딩테스트 연습 >  연습문제 > 평균 구하기

def solution(arr):
    sum = 0
    for i in range(len(arr)) :
        sum += arr[i]
    answer = sum / len(arr)
    return answer