def solution(data, ext, val_ext, sort_by):
    if ext == 'code': cri = 0
    elif ext =='date' :cri=1
    elif ext=='maximum' : cri=2
    else : cri = 3
    answer = [num for num in data if num[cri] < val_ext ]

    if sort_by == 'code': sortd = 0
    elif sort_by =='date' :sortd=1
    elif sort_by=='maximum' : sortd=2
    else : sortd = 3
    answer.sort(key=lambda x:x[sortd])
    return answer