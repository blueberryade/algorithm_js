import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x,y):
    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, -1, 1, -1, 1, 1, -1]

    graph[x][y] = 0
    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <=nx<h and 0<=ny<w and graph[nx][ny] == 1 :
            dfs(nx,ny)

while True:
    cnt = 0
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break

    graph = [list(map(int,input().split())) for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i,j)
                cnt+=1
    print(cnt)         
