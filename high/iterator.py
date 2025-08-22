
# 迭代器 Iterator

# 1. 集合数据类型
# 2. generator
# 3. 可迭代对象 Iterable

from collections.abc import Iterable

print('[]', isinstance([], Iterable))

print('{}', isinstance({}, Iterable))

print('abc', isinstance('acb', Iterable))

print('(x for x in range(10))', isinstance((x for x in range(10)), Iterable))

print(100, isinstance(100, Iterable))


print('-------- iterator -----------------')

from collections.abc import Iterator

print('(x for x in range(10))', isinstance((x for x in range(10)), Iterator))

print('[]', isinstance([], Iterator))

print('{}', isinstance({}, Iterator))

print('abc', isinstance('acb', Iterator))

# 生成器都是 Iterator 对象，但 list dict str 虽然是 Iterable, 却不是 Iterator

# iter()函数

#Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

print('----------------- practice ------------')

for x in [1, 3, 3, 5]:
  pass

# 相当于

it = iter([1, 3, 3, 5])

while True:
  try:
    x = next(it)
    print(x)
  except StopIteration:
    break