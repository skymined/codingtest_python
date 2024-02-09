# https://school.programmers.co.kr/learn/courses/30/lessons/12930
# 코딩테스트 연습 > 연습문제 > 이상한 문자 만들기

# 문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다.
# 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

def solution(s):
    answer = s.split()
    yepp =[]
    for i in answer :
        new = ''
        for j in range(len(i)):
            if j== 0  or j % 2 == 0 : # 짝수이거나 0인 경우
                new += i[j].upper()
            elif j % 2!= 0 : # 홀수
                new+= i[j].lower()
        yepp.append(new) 
    return ' '.join(yepp)


solution("try etry try")


# 알고리즘 자체에 무슨 문제가 있는지 모르겠음