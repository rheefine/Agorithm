# 11650 좌표 정렬하기

n = int(input())

x_y_lists = [list (map(int, input().split(" "))) for _ in range(n)]

sorted_x_y = sorted(x_y_lists, key = lambda x:(x[0], x[1]))

for i in range(n):
    print(sorted_x_y[i][0], sorted_x_y[i][1])
