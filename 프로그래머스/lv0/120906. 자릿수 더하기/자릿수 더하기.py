def solution(n):
    li = []
    answer = 0
    li = str(n)
    for i in range(len(li)):
         answer = answer + int(li[i])
    return answer