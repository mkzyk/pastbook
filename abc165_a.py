#https://atcoder.jp/contests/abc165/tasks/abc165_a

K = int(input())
A,B = map(int, input().split())

isOK = False
for i in range(A, B+1):
    if i % K == 0:
        isOK = True
        break

if isOK:
    print("OK")
else:
    print("NG")