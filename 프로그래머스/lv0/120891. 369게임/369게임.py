def solution(order):
    answer = 0
    a = str(order)
    for i in a:
        if i == '3':
            answer += 1
        elif i == '6':
            answer += 1
        elif i == '9':
            answer += 1
    return answer