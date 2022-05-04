#https://atcoder.jp/contests/abc088/tasks/abc088_c
grid = []
for _ in range(0,3):
    tmp_row = list(map(int, input().split()))
    grid.append(tmp_row)

ans = True

if grid[0][0] - grid[0][1] != grid[1][0] - grid[1][1] or grid[1][0] - grid[1][1] != grid[2][0] - grid[2][1]:
    ans = False

if grid[0][1] - grid[0][2] != grid[1][1] - grid[1][2] or grid[1][1] - grid[1][2] != grid[2][1] - grid[2][2]:
    ans = False

if grid[0][0] - grid[1][0] != grid[0][1] - grid[1][1] or grid[0][1] - grid[1][1] != grid[0][2] - grid[1][2]:
    ans = False

if grid[1][0] - grid[2][0] != grid[1][1] - grid[2][1] or grid[1][1] - grid[2][1] != grid[1][2] - grid[2][2]:
    ans = False

if ans:
    print("Yes")
else:
    print("No")