def solution(i, j, k):
    answer = 0
    a = []
    for b in range(j):
        if b >= i-1:
            a += str(b+1)
    answer = a.count(str(k))
    return answer