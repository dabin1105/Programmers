def solution(my_string):
    b =''
    for i in my_string:
        if i.islower() == 1:
            b += i.upper()
        if i.isupper() == 1:
            b += i.lower()
    return b