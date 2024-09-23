# https://school.programmers.co.kr/learn/courses/30/lessons/12982
# 코딩테스트 연습 > Summer/Winter Coding > 예산

# 자연수 n이 매개변수로 주어집니다.
# n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.


def solution(d, budget):
    d.sort()
    answer = 0
    for i in range(len(d)):
        budget -= d[i]
        answer +=1
        if budget <0 :
            answer -=1
            break
    return answer

solution([1,3,2,5,4],9)
pass

