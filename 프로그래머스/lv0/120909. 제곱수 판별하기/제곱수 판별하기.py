import math
def solution(n):
    a = math.sqrt(n)
    if(a%1 == 0):
        answer = 1
    else:
        answer = 2
    return answer