# 용액 2467

n = int(input())
liquids = list(map(int, input().split()))

result = float("inf")
liquid_1, liquid_2 = 0, n - 1

for i in range(n - 1):
    left = i + 1
    right = n - 1

    while left <= right:
        mid = (left + right) // 2
        mix = liquids[mid] + liquids[i]

        if abs(mix) < result:
            liquid_1 = i
            liquid_2 = mid
            result = abs(mix)
        
        if mix == 0:
            break
        elif mix < 0:
            left = mid + 1
        else:
            right = mid - 1

print(liquids[liquid_1], liquids[liquid_2])
