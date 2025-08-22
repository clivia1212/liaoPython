# 生成器

L = [x * x for x in range(10)]

print(L)

g = (x * x for x in range(10))

print(next(g))

print(next(g))

print(next(g))

print(next(g))


print('------- 斐波拉契数列 ---------')

# 1，1，2，3，5，8，13，21，34，...

def fib(max):
  n, a, b = 0, 0, 1
  while n < max:
    print(b)
    a, b = b, a + b
    n = n + 1
  return 'done'

print(fib(6))


print('------- 斐波拉契数列 generator函数 关键字 yield ---------')

def fib2(max):
  n, a, b = 0, 0, 1
  while n < max:
    yield b
    a, b = b, a + b
    n = n + 1
  return 'done'

# print(fib2(6))

g = fib2(6)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


print('------- for return StopIteration ----------')

while True:
  try:
    x = next(g)
    print('g:', x)
  except StopIteration as e:
    print('Generator return value:', e.value)
    break

print('--------- practice 杨辉三角 ------------')

def triangles():
  L = [1]
  yield L

  while True:
    Ln = []
    for i in range(len(L) + 1):
      if i == 0 or i == len(L):
        Ln.append(1)
      else:
        Ln.append(L[i] + L[i - 1])
    L = Ln
    yield Ln



# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')

