#nieskonczone
import time


def naive(S, W):
    t_start = time.perf_counter()
    m = 0
    i = 0
    W_found = 0
    count = 0
    w_len = len(W)
    s_len = len(S)
    found_idx = list()
    while m < s_len - w_len + 1:
        i = 0
        while True:
            count += 1
            if W[i] == S[m + i]:
                i += 1
                if i >= w_len:
                    found_idx.append(m)
                    W_found += 1
                    break
            else:
                break
        m += 1
    t_stop = time.perf_counter()
    return W_found, count, t_stop - t_start, found_idx

def hash_(word, N):
    d = 256
    q = 101
    hw = 0
    for i in range(N):  # N - to długość wzorca
        hw = (hw * d + ord(word[i])) % q
        # dla d będącego potęgą 2 można mnożenie zastąpić shiftem uzyskując pewne przyspieszenie obliczeń
    return hw


def Rabin_Karp(S, W):
    t_start = time.perf_counter()
    count = 0
    found_idx = list()
    M = len(S)
    N = len(W)
    hW = hash_(W, N)
    W_found = 0
    for m in range(M - N + 1):
        count += 1
        hS = hash_(S[m:m + N], N)
        if hS == hW:
            if S[m:m + N] == W:
                W_found += 1
                found_idx.append(m)
    t_stop = time.perf_counter()
    return W_found, count, t_stop - t_start, found_idx


def Rabin_Karp_rolling_hash(S, W):
    t_start = time.perf_counter()
    d = 256
    q = 101
    h = 1
    N = len(W)
    for i in range(N - 1):
        h = (h * d) % q

    count = 0
    collision_count = 0
    found_idx = list()
    M = len(S)
    hW = hash_(W, N)
    W_found = 0
    m = 0
    while m < M - N + 1:
        if m == 0:
            hS = hash_(S[:N], N)
            count += 1
            m += 1
            if hS == hW:
                if S[:N] == W:
                    W_found += 1
                    found_idx.append(0)
            continue
        count += 1
        hS = (d * (hS - ord(S[m - 1]) * h) + ord(S[m - 1 + N])) % q
        if hS < 0:
            hS += q
        if hS == hW:
            if S[m:m + N] == W:
                W_found += 1
                found_idx.append(m)
            else:
                collision_count += 1
        m += 1
    t_stop = time.perf_counter()
    return W_found, count, t_stop - t_start, found_idx, collision_count


def KMP_table(W):
    pos = 1
    cnd = 0
    len_W = len(W)
    T = [0 for _ in range(len_W)]
    T[0] = -1

    while pos < len_W:
        if W[pos] == W[cnd]:
            T[pos] = T[cnd]
        else:
            T[pos] = cnd
            while cnd >= 0 and W[pos] != W[cnd]:
                cnd = T[cnd]
        pos += 1
        cnd += 1
    return T

def KMP(S, W):
    t_start = time.perf_counter()
    m = 0
    i = 0
    T = KMP_table(W)
    nP = 0
    P = list()
    len_S = len(S)
    len_W = len(W)
    count = 0

    while m < len_S:
        count += 1
        if W[i] == S[m]:
            m += 1
            i += 1
            if i == len_W:
                P.append(m - i)
                nP += 1
                i = T[i - 1]
        else:
            i = T[i]
            if i < 0:
                m += 1
                i += 1
    t_stop = time.perf_counter()
    return nP, count, t_stop - t_start, P, T


def main():
    with open("lotr.txt", encoding='utf-8') as f:
        text = f.readlines()

    S = ' '.join(text).lower()
    W = 'time.'
    N = len(W)

    W_found1, count1, time1, found_idx1 = naive(S, W)
    print(W_found1,';',count1)

    W_found2, count2, time2, found_idx2, collisions2 = Rabin_Karp_rolling_hash(S, W)
    print(W_found2, ';', count2, ';', collisions2)

    W_found3, count3, time3, found_idx3, T_table = KMP(S, W)
    print(W_found3, ';', count3, ';', T_table)

main()