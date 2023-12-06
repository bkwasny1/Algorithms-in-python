#skończone

def string_compare(P, T, i, j):
    if i == 0:
        return j
    if j == 0:
        return i

    zamian = string_compare(P, T, i - 1, j - 1) + (P[i] != T[j])
    wstawien = string_compare(P, T, i, j - 1) + 1
    usuniec = string_compare(P, T, i - 1, j) + 1

    return min(zamian, wstawien, usuniec)


def PD(P, T):
    D = [[i if j == 0 else 0 for i in range(len(T))] for j in range(len(P))]
    for i in range(len(D)):
        D[i][0] = i
    Parrents = [['X' for i in range(len(T))] for j in range(len(P))]
    for i in range(1, len(Parrents)):
        Parrents[0][i] = 'I'
        Parrents[i][0] = 'D'

    for i in range(1, len(D)):
        for j in range(1, len(D[i])):
            zamian = D[i - 1][j - 1] + (P[i] != T[j])
            wstawien = D[i][j - 1] + 1
            usuniec = D[i - 1][j] + 1
            tab = [zamian, wstawien, usuniec]
            min_ = min(zamian, wstawien, usuniec)
            D[i][j] = min_
            idx = -1
            for k in range(3):
                if min_ == tab[k]:
                    idx = k
                    break
            if idx == 0:
                if T[j] == P[i]:
                    Parrents[i][j] = 'M'
                else:
                    Parrents[i][j] = 'S'
            if idx == 1:
                Parrents[i][j] = 'I'
            if idx == 2:
                Parrents[i][j] = 'D'
    return D[-1][-1], Parrents


def get_path(Parrents):
    path = list()
    i = len(Parrents) - 1
    j = len(Parrents[0]) - 1

    while Parrents[i][j] != 'X':
        path.append(Parrents[i][j])
        if Parrents[i][j] == 'M' or Parrents[i][j] == 'S':
            i -= 1
            j -= 1
        elif Parrents[i][j] == 'I':
            j -= 1
        elif Parrents[i][j] == 'D':
            i -= 1
    path.reverse()
    string = ""
    for elem in path:
        string += elem
    return string


def matching_strings(P, T):
    D = [[0 for i in range(len(T))] for j in range(len(P))]
    for i in range(len(D)):
        D[i][0] = i
    Parrents = [['X' for i in range(len(T))] for j in range(len(P))]
    for i in range(1, len(Parrents)):
        Parrents[i][0] = 'D'
    for i in range(1, len(D)):
        for j in range(1, len(D[i])):
            zamian = D[i - 1][j - 1] + (P[i] != T[j])
            wstawien = D[i][j - 1] + 1
            usuniec = D[i - 1][j] + 1
            tab = [zamian, wstawien, usuniec]
            min_ = min(zamian, wstawien, usuniec)
            D[i][j] = min_
            idx = -1
            for k in range(3):
                if min_ == tab[k]:
                    idx = k
                    break
            if idx == 0:
                if T[j] == P[i]:
                    Parrents[i][j] = 'M'
                else:
                    Parrents[i][j] = 'S'
            if idx == 1:
                Parrents[i][j] = 'I'
            if idx == 2:
                Parrents[i][j] = 'D'
    min_val = 9999999999999
    end_idx = 0
    for i in range(len(D[-1])):
        if D[-1][i] < min_val:
            min_val = D[-1][i]
            end_idx = i
    started_idx = end_idx - len(P) + 2
    return end_idx, started_idx


def get_sec(Parrents, P):
    sec = list()
    i = len(Parrents) - 1
    j = len(Parrents[0]) - 1

    while Parrents[i][j] != 'X':
        if Parrents[i][j] == 'M':
            sec.append(P[i])
            i -= 1
            j -= 1
        elif Parrents[i][j] == 'S':
            i -= 1
            j -= 1
        elif Parrents[i][j] == 'I':
            j -= 1
        elif Parrents[i][j] == 'D':
            i -= 1
    sec.reverse()
    string = ""
    for elem in sec:
        string += elem
    return string


def longest(P, T):
    D = [[i if j == 0 else 0 for i in range(len(T))] for j in range(len(P))]
    for i in range(len(D)):
        D[i][0] = i
    Parrents = [['X' for i in range(len(T))] for j in range(len(P))]
    for i in range(1, len(Parrents)):
        Parrents[0][i] = 'I'
        Parrents[i][0] = 'D'

    for i in range(1, len(D)):
        for j in range(1, len(D[i])):
            zamian = D[i - 1][j - 1]
            if P[i] != T[j]:
                zamian += 9999999
            wstawien = D[i][j - 1] + 1
            usuniec = D[i - 1][j] + 1
            tab = [zamian, wstawien, usuniec]
            min_ = min(zamian, wstawien, usuniec)
            D[i][j] = min_
            idx = -1
            for k in range(3):
                if min_ == tab[k]:
                    idx = k
                    break
            if idx == 0:
                if T[j] == P[i]:
                    Parrents[i][j] = 'M'
                else:
                    Parrents[i][j] = 'S'
            if idx == 1:
                Parrents[i][j] = 'I'
            if idx == 2:
                Parrents[i][j] = 'D'
    return get_sec(Parrents, P)


def sort_t(T):
    string = ' '
    sorted = list()
    for i in range(1, len(T)):
        sorted.append(int(i))
    sorted.sort()
    for elem in sorted:
        string += str(elem)
    return string


P = ' kot'
T = ' pies'
min_ = string_compare(P, T, len(P) - 1, len(T) - 1)
print(min_)


P = ' biały autobus'
T = ' czarny autokar'
min_, _ = PD(P, T)
print(min_)


P = ' thou shalt not'
T = ' you should not'
min_, parrents = PD(P, T)
print(get_path(parrents))


P = ' ban'
T = ' mokeyssbanana'
end_idx, started_idx = matching_strings(P, T)
print(started_idx)


P = ' democrat'
T = ' republican'
sec = longest(P, T)
print(sec)


T = ' 243517698'
P = sort_t(T)
sec = longest(P, T)
print(sec)