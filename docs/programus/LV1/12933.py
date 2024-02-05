# https://school.programmers.co.kr/learn/courses/30/lessons/12933
# 코딩테스트 연습 >  연습문제 > 정수 내림차순으로 배치하기

# 함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.


def solution(n):
    n = [ i for i in str(n) ]
    n.sort()
    n.reverse()
    answer = ''.join(i for i in n)
    return int(answer)

solution(118372)

