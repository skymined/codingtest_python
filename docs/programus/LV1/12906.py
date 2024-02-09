# https://school.programmers.co.kr/learn/courses/30/lessons/12906
# 코딩테스트 연습 > 스택/큐 > 같은 숫자는 싫어

# 배열 arr가 주어집니다. 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다.
# 이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다.
# 단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다.

def solution(arr):
    answer = []
    for i in range(len(arr)-1) :
        if arr[i] != arr[i+1] :
            answer.append(arr[i])
        else :
            pass
    answer.append(arr[-1])
    return answer

solution([1,1,3,3,0,1,1])
pass

