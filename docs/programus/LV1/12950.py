# https://school.programmers.co.kr/learn/courses/30/lessons/12950
# 코딩테스트 연습 > 연습문제 > 문자열 다루기 기본
# 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다.
# 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.


def solution(arr1, arr2):
    answer=[]
    for i in range(len(arr1)):
        sub_list = []
        for j in range(len(arr1[i])) :
            sub_list.append(arr1[i][j]+arr2[i][j])
        answer.append(sub_list)
    return answer

solution([[1,2],[2,3]], [[3,4],[5,6]])
pass
