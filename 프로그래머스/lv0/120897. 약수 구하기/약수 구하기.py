def solution(n):
    answer = []
    for i in range(int(n)):
        if int(n)%(i+1) == 0:
            answer.append(i+1)
    return answer