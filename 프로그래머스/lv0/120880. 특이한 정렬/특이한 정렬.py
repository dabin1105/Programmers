def solution(numlist, n):
    answer = []
    if n in numlist:
        answer.append(n)
    for i in range(10000):
        b = n+(i+1)
        c = n-(i+1)
        if b in numlist:
            answer.append(b)
        if c in numlist:
            answer.append(c)
    return answer