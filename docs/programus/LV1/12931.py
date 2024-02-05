# https://school.programmers.co.kr/learn/courses/30/lessons/12931
# 코딩테스트 연습 >  연습문제 > 나머지가 1이 되는 수 찾기

# 자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요. 예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.


def solution(n):
    n = str(n)
    answer = 0
    for i in range(len(n)):
        answer += int(n[i])
    return answer

solution(123)

