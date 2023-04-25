
from sys import stdin

t = int(input())
n = [int(stdin.readline()) for _ in range(t)]

num_list =[1,2,4]

for i in range(3,max(n)):
    last_num = num_list[i-1] + num_list[i-2] + num_list[i-3]
    num_list.append(last_num)

for i in n:
    print(num_list[i-1])