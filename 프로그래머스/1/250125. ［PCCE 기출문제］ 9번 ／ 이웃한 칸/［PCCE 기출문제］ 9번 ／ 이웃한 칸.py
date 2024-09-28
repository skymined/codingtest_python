def solution(board, h, w):
    n = len(board)
    answer = 0
    dh = [0,1,-1,0]
    dw = [1,0,0,-1]
    middle = board[h][w]
    for i in range(4):
        around = [h+dh[i], w+dw[i]]
        if around[0] >= 0 and around [0] < n and around[1] >= 0 and around[1] < n :
            if middle == board[around[0]][around[1]] :
                answer +=1
    return answer