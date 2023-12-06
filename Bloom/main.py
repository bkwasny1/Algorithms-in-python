#skończone
import math
import time


def hash_(word, N):
    d = 256
    q = 101
    hw = 0
    for i in range(N):
        hw = (hw * d + ord(word[i])) % q
    return hw


def RabinKarpSet(S, subs, N):
    t_start = time.perf_counter()
    d = 256
    q = 101
    n = 20
    P = 0.001
    b = -n * math.log(P) / (math.log(2) ** 2)
    k = b / n * math.log(2)
    b = int(b)
    k = int(k)
    M = len(S)
    hsubs = {}
    bloom_filter = [0] * b

    for sub in subs:
        h = hash_(sub[:N], N)
        if h not in hsubs:
            hsubs[h] = []
        hsubs[h].append(sub)
        for i in range(k):
            gi = (h + i * hash_(sub[:N], N)) % b
            bloom_filter[gi] = 1

    sub_found = {}
    hs = hash_(S[:N], N)
    if bloom_filter[hs] == 1:
        for sub in hsubs[hs]:
            if S[:N] == sub:
                if sub not in sub_found:
                    sub_found[sub] = 1
                else:
                    sub_found[sub] += 1

    for m in range(1, M - N + 1):
        hs = (hs - (ord(S[m - 1]) * (d ** (N - 1)) % q)) % q
        hs = (hs * d + ord(S[m + N - 1])) % q
        if bloom_filter[hs] == 1:
            if hs in hsubs:
                for sub in hsubs[hs]:
                    if S[m:m + N] == sub:
                        if sub not in sub_found:
                            sub_found[sub] = 1
                        else:
                            sub_found[sub] += 1
        else:
            continue

    t_stop = time.perf_counter()
    return sub_found, t_stop - t_start


def main():
    with open("lotr.txt", encoding='utf-8') as f:
        text = f.readlines()

    S = ' '.join(text).lower()
    subs = ['gandalf', 'looking', 'blocked', 'comment', 'pouring', 'finally', 'hundred', 'hobbits', 'however',
            'popular', 'nothing', 'enjoyed', 'stuffed', 'relaxed', 'himself', 'present', 'deliver', 'welcome',
            'baggins', 'further']
    N = len(subs[0])

    x = RabinKarpSet(S, subs, N)
    for i in subs:
        print(i, x[0][i])

main()

