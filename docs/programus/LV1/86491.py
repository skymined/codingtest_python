# https://school.programmers.co.kr/learn/courses/30/lessons/86491
# 코딩테스트 연습 > 완전탐색 > 최소직사각형

# 모든 명함의 가로 길이와 세로 길이를 나타내는 2차원 배열 sizes가 매개변수로 주어집니다.
# 모든 명함을 수납할 수 있는 가장 작은 지갑을 만들 때, 지갑의 크기를 return 하도록 solution 함수를 완성해주세요.

def solution(sizes):
    [items.sort() for items in sizes]
    answer = [0,0]
    for i in range(len(sizes)) :
        if sizes[i][0] > answer[0]:
            answer[0] = sizes[i][0]
        else :
            pass
    for j in range(len(sizes)) :
        if sizes[j][1] > answer[1]:
            answer[1] = sizes[j][1]
        else :
            pass
    return answer[0] * answer[1]

solution([[60, 50], [30, 70], [60, 30], [80, 40]])
pass

# max(x[0] for x in sizes) * max([x[1] for x in sizes])
# max(x) 는 x리스트 안에서 가장 큰 값을 가지고 옴!