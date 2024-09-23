# https://school.programmers.co.kr/learn/courses/30/lessons/12932
# 코딩테스트 연습 >  연습문제 > 자연수 뒤집어 배열로 만들기

# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.


def solution(n):
    n= str(n)
    answer = []
    [answer.append(int(n[i])) for i in range(len(n))]
    answer.reverse()
    return answer

solution(123)

