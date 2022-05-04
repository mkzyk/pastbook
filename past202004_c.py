str = []
N = int(input())
for i in range(0,N):
    tmp = list(input())
    str.append(tmp)

# 列の一番下から１つ上から一番上までループ
for i in range(N-2, -1, -1):
    # 行の２つめの文字からループ
    for j in range(1, N*2-1):
        if str[i][j] == '#':
            if str[i+1][j] == 'X' or str[i+1][j-1] == 'X' or str[i+1][j+1] == 'X':
                str[i][j] = 'X'

for i in range(0,N):
    str[i] = ''.join(str[i])
    print(str[i])
                