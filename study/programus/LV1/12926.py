# https://school.programmers.co.kr/learn/courses/30/lessons/12926
# 코딩테스트 연습 > 연습문제 > 시저 암호

# 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 
# 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다.
# "z"는 1만큼 밀면 "a"가 됩니다. 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

import string
alphabet_lower = string.ascii_lowercase
alphabet_upper = string.ascii_uppercase

def solution(s, n):
    for i in  range(len(s)):
        if i in string.ascii_lowercase :
            index = alphabet_lower.index(i)
            index += n
            if index > 26 :
                index -= 26
            i = alphabet_lower(index)
        elif i in alphabet_upper :
            index = alphabet_upper.index(i)
            index += n
            if index > 26 :
                index -= 26
            i = alphabet_upper(index)
    return s

solution("AB",1)

