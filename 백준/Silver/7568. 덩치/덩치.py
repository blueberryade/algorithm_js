import sys
input = sys.stdin.readline

N = int(input())
lst = []

for _ in range(N):
    x,y = map(int,input().split())
    lst.append((x,y))   

for i in lst:
    rank = 1
    for j in lst:
        if i[0] < j[0] and i[1] < j[1]:
            rank+=1
    print(rank,end=' ')
