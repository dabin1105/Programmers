def solution(quiz):
    c = []
    answer = []
    for i in range(len(quiz)):
        b = quiz[i].find("=")
        c.append(quiz[i][:b])
        if str(eval(c[i])) == quiz[i][b+2:]:
            answer.append("O")
        else:
            answer.append("X")
        print(eval(c[i]))
        print(quiz[i][b+2:])
    return answer