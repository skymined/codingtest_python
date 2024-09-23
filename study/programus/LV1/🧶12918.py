# https://school.programmers.co.kr/learn/courses/30/lessons/12918
# 코딩테스트 연습 > 연습문제 > 문자열 다루기 기본



def solution(s):
    if len(s) ==4 or 6 :
        try : 
            s = int(s)
            answer = True
        except :
            answer= False
    else :
        answer = False
    return answer

solution("1234")
pass
