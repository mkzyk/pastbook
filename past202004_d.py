#https://atcoder.jp/contests/past202004-open/tasks/past202004_d

def is_match(T, S):
    # input文字列(S)と作成文字列(T)の差分文字数分をループ
    # 差分文字分だけにして、あとで作成文字列(T)を足すことでinput文字列分を全文字参照できる
    # input文字列(S)よりも作成文字列(T)のほうが文字数が大きい場合はループをしない（検証する意味がないので）
    for i in range(0, len(S)-len(T)+1):
        ok = True
        # 作成文字列分(T)を一文字ずつループ
        for j in range(0, len(T)):
            if S[i+j] != T[j] and T[j] != ".":
                ok = False
        if ok:
            return True
    return False

S = input()

C = "abcdefghijklmnopqrstuvwxyz."
M = []

for T in C:
    if is_match(T, S):
        M.append(T)

for c1 in C:
    for c2 in C:
        T = c1 + c2
        if is_match(T, S):
            M.append(T)

for c1 in C:
    for c2 in C:
        for c3 in C:
            T = c1 + c2 + c3
            if is_match(T, S):
                M.append(T)

print(len(M))                