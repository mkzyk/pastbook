#https://atcoder.jp/contests/arc046/tasks/arc046_a

N = int(input())
digit = 0
for i in range(1, 555555+1):
    si = str(i)
    isZorome = True
    for s in si:
        if s != si[0]:
            isZorome = False
    if isZorome:
        digit += 1
    if isZorome and digit == N:
        print(si)
        break

