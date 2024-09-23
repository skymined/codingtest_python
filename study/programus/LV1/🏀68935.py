# https://school.programmers.co.kr/learn/courses/30/lessons/68935
# 코딩테스트 연습 > 월간 코드 챌린지 시즌1 > 3진법 뒤집기

# 자연수 n이 매개변수로 주어집니다.
# n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

# def solution(n):
#     base3 = []
#     while True :
#         base3.append(n % 3) 
#         n = n//3
#         if n ==1 :
#             base3.append(1)
#             break
#     answer = 0
#     for i in range(1,len(base3)+1):
#         answer += 3**(i-1)*(base3[-i])
#     return answer

def solution(n):
    answer = 0
    while n > 0:
        answer *= 3
        answer += (n % 3)
        n //= 3
    return answer

# 미친 알고리즘



solution(125)
pass

