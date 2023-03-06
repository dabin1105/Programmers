def solution(num, total):
    li = []
    if num%2 == 0:
        for i in range(num):
            a = int(total/num)-int(num/2) +i+1
            li.append(a)
    elif num%2 != 0:
        for j in range(num):
            a = int(total/num)-int(num/2)+j
            li.append(a)
    else:
        li.append(0)
            
    return li

