def solution(num, k):
    result = str(num).find(str(k))
    if result > -1:
        result = result+1
    else:
        result = -1
    return result