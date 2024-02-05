# https://school.programmers.co.kr/learn/courses/30/lessons/12910
# 코딩테스트 연습 >  연습문제 > 나누어 떨어지는 숫자 배열

# array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
# divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.

def solution(arr, divisor):
    answer=[]
    for i in range(len(arr)):
        if arr[i] % divisor == 0 :
            answer.append(arr[i])
    if answer == [] :
        answer = [-1]
    answer.sort()
    return answer

solution([5, 9, 7, 10], 5)
pass
