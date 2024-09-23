# https://school.programmers.co.kr/learn/courses/30/lessons/12903
# 코딩테스트 연습 >  연습문제 > 가운데 글자 가져오기

# 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

def solution(s):
    leng = len(s)
    if leng % 2 ==0 :
        leng = leng //2 
        answer = s[(leng-1)] + s[leng]
    elif leng %2 != 0:
        leng = leng //2
        answer = s[leng]
    return answer


solution("qwer")
pass
