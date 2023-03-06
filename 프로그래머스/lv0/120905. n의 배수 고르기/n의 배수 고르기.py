def solution(n, numlist):
    answer = []
    li =[]
    n <= 10000
    for i in range(10000):
        li.append(n*(i+1))
        
    print(li)
    for s in range(len(numlist)):
        if numlist[s] in li:
            answer.append(numlist[s])
    return answer