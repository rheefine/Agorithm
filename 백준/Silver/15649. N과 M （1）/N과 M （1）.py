n, m = map(int, input().split())

k = []

def func():
  if len(k) == m:
    print(' '.join(map(str, k)))
    return

  for i in range(1, n + 1):
    if i in k:
      continue
    k.append(i)
    func()
    k.pop()

func()