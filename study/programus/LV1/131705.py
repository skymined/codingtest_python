# https://school.programmers.co.kr/learn/courses/30/lessons/131705
# 코딩테스트 연습 > 연습문제 > 삼총사

# 5명의 학생이 있고, 각각의 정수 번호가 순서대로 -2, 3, 0, 2, -5일 때
# 첫 번째, 세 번째, 네 번째 학생의 정수 번호를 더하면 0이므로 세 학생은 삼총사입니다.
# 서로 다른 학생의 정수 번호가 같을 수 있습니다.

def solution(number):
    answer = 0
    while len(number) >=3 :
        num = number[1] + int([i for i in number]) + int([i for i in number])
        if num == 0 :
            answer +=1
        answer = int(answer/2)
        number.remove(number[1])
    return answer


solution([-2, 3, 0, 2, -5])
pass

# from itertools import combinations 모듈 사용할 수도 있음
# 