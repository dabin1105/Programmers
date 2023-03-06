def solution(score):
    a = list(score)
    b = []
    for i in range(len(score)):
        a[i] = sum(score[i])/2
    for i in a:
        b.append(sorted(a,reverse = True).index(i)+1)
    return b