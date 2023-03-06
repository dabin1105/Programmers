def solution(id_pw, db):
    for i in range(len(db)):
        if id_pw in db:
            answer = 'login'
        elif id_pw[0] in db[i]:
            answer = 'wrong pw'
            break;
        else:
            answer = 'fail'
    return answer