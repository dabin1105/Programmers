def solution(array, n):
    answer = 0
    for i in range(100-n):
        b = n + i
        c = n - i
        if c in array:
            answer = c
            break
        elif b in array:
            answer = b
            break
    return answer