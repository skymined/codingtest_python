# https://school.programmers.co.kr/learn/courses/30/lessons/12934
# 코딩테스트 연습 >  연습문제 > 정수 제곱근 판별

# 임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
# n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.


def solution(n):
    answer = 0
    for x in range(1,n+1):
        if x**2 == n :
            answer = (x+1)**2
            break
        else : 
            pass
    if answer == 0 :
        answer = -1
    return answer

solution(9)

