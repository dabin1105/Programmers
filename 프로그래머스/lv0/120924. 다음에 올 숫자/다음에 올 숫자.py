def solution(common):
    a=0
    for i in range((len(common)-2)):
        if (common[i+1] - common[i]) == (common[i+2] - common[i+1]):
            a = common[1] - common[0]
            answer = common[-1]+a
        elif(common[i+1] - common[i]) != (common[i+2] - common[i+1]):
            n = common[i+1]/common[i]
            answer = common[-1]*n
        
    return answer