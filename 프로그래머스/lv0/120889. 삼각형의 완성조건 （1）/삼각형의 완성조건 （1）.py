def solution(sides):
    answer = 0
    a = sorted(sides)
    if a[0]+a[1] > a[2]:
        answer = 1
    elif a[0] + a[1] <= a[2]:
        answer = 2
    return answer