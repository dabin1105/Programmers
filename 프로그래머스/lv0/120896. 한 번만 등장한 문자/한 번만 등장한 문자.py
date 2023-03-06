def solution(s):
    answer = ''
    for i in range(len(s)):
        a = s.find(s[i])
        if s[i] not in s[1:a-1]:
            if s[i] not in s[a+1:]:
                    answer += s[i]
    
    return ''.join(sorted(answer))