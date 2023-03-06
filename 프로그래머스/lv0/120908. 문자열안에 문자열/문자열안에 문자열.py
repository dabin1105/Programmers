def solution(str1, str2):
    a = str1.find(str2)
    if a== -1:
        answer = 2
    else:
        answer = 1
    return answer