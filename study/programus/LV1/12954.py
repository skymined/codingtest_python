# https://school.programmers.co.kr/learn/courses/30/lessons/87389
# 코딩테스트 연습 >  연습문제 > 나머지가 1이 되는 수 찾기

# 자연수 n이 매개변수로 주어집니다. n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성해주세요. 답이 항상 존재함은 증명될 수 있습니다.


def solution(n):
    answer = []
    for x in range(1,n):
        if n%x ==1 :
            answer.append(x)
    return answer[0]

solution(10)