t = int(input())
n = list(map(int, input().split(' ')))

for i in range(t):
    divisor_list = []
    for j in range(1, n[i]):
        if n[i]%j==0:
            divisor_list.append(j)

    if sum(divisor_list) == n[i]:
        print('Perfect')
    
    if sum(divisor_list) < n[i]:
        print('Deficient')

    if sum(divisor_list) > n[i]:
        print('Abundant')
