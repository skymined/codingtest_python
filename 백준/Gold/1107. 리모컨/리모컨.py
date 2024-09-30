N_origin = int(input()) # 목표 채널
n = int(input()) # 고장난 버튼의 개수

if n>0 : # 고장난 버튼이 있는 경우
    numbers = list(map(int, input().split()))
else : 
    numbers =[]

min_clicks = abs(N_origin-100)

able = [item for item in range(10) if item not in numbers]

for i in range(1000000):
    str_n = str(i) # i는 누르는 숫자, N_origin은 목표 채널
    # i에 고장난 숫자가 포함되지 않을 경우
    if all(int(j) in able for j in str_n) :
        min_clicks = min(min_clicks,len(str_n)+abs(i-N_origin))

print(min_clicks)