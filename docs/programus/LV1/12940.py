# https://school.programmers.co.kr/learn/courses/30/lessons/12940
# 코딩테스트 연습 > 연습문제 > 문자열 다루기 기본

# 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 
# 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.


def solution(n, m):
    if n > m :
        n, m = m, n
    # 최대공약수
    duplicate =[]
    answer = []
    for i in range(2,n+1):
        if n%i ==0 :
            if m%i ==0 :
                duplicate.append(i)
    if len(duplicate) == 0 :
        answer.append(1)
    else : 
        answer.append(duplicate[-1])

    # 최소공배수
    num=0
    while True :
        num += 1
        m_1 = m *num
        if m_1 % n == 0 :
            answer.append(m_1)
            break
        else : 
            pass
    return answer

solution(17,200)
pass

