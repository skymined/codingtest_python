# https://school.programmers.co.kr/learn/courses/30/lessons/12916
# 코딩테스트 연습 >  연습문제 > 문자열 내 p와 y의 개수
# 대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

# 예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.


def solution(s):
    y_num = 0
    p_num = 0
    for i in range(len(s)):
        if s[i] == 'y' or s[i] == 'Y' :
            y_num +=1
        elif s[i] == 'p' or s[i] =='P' :
            p_num +=1
        else :
            pass
    if y_num == 0  and p_num ==0 :
        result = True
    elif y_num == p_num :
        result = True
    elif y_num != p_num :
        result = False

    return result

solution('Pyy')

