# https://school.programmers.co.kr/learn/courses/30/lessons/12947
# 코딩테스트 연습 >  연습문제 > 정수 내림차순으로 배치하기

# 양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다.
# 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다.
# 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

def solution(x):
    # 각 자리 수를 더하기
    x = str(x)
    data = [int(x[i]) for i in range(0,len(x))]
    sum =0 
    for num in data:
        sum += num    
    # if 문 사용
    if int(x) % sum  == 0 :
        answer = True
    else :
        answer = False
    return answer
        
    

solution(18)

