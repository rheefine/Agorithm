# 11725 트리의 부모찾기

import sys
sys.setrecursionlimit(10**6)
n = int(input())

graph = [[] for _ in range(n+1)]
for i in range(n-1):
    point1, point2 = map(int, input().split())
    graph[point1].append(point2)
    graph[point2].append(point1)

visited = [0] * (n+1)

def dfs(s):
    for i in graph[s]:
        if visited[i] == 0:
            visited[i] = s
            dfs(i)

dfs(1)

for i in range(2, n+1):
    print(visited[i])
