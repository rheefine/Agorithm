n = int(input())
sequence = list(map(int,input().split()))

for i in range(1, n):
    sequence[i] = max(sequence[i], sequence[i-1] + sequence[i])

print(max(sequence))