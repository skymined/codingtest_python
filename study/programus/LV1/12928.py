# https://school.programmers.co.kr/learn/courses/30/lessons/12928
# 코딩테스트 연습 >  연습문제 > 약수의 합

def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n % i == 0 :
            answer += i
        else :
            pass    
    return answer

solution(12)