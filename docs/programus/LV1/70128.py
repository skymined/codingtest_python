# https://school.programmers.co.kr/learn/courses/30/lessons/70128
# 코딩테스트 연습 > 월간 코드 챌린지 시즌1

# 길이가 같은 두 1차원 정수 배열 a, b가 매개변수로 주어집니다. a와 b의 내적을 return 하도록 solution 함수를 완성해주세요.
# 이때, a와 b의 내적은 a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1] 입니다. (n은 a, b의 길이)

def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer

solution([1,2,3,4], [-3,-1,0,2])
pass
