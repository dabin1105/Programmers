def solution(A, B):
    if A == B:
        answer = 0
    else :
        for i in range(len(A)):
            A = A[-1]+A[:-1]
            if A == B:
                answer = i+1
                break
            elif A != B:
                answer = -1
    return answer