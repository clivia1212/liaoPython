
# 列表生成式

print(list(range(1, 11)))

list1 = [x * x for x in range(1, 11)]

list2 = [x * x for x in range(1, 11) if x % 2 == 0]

print('list1', list1)
print('list2', list2)

print('------- 双层循环 -------')

list3 = [m + n for m in 'ABC' for n in '123']

print('list3', list3)

import os

dirs = [d for d in os.listdir('.')]

print('dirs', dirs)

print('------- for 多个变量 -------')

d = { 'x': 'A', 'y': 'B', 'z': 'C' }

print([ k + '=' + v for k, v in d.items()])


print('------- list中所有字符变成小写 -------')

list4 = ['A', 'Video', 'Apple', 'hello']

print([s.lower() for s in list4])

print('------- 列表生成式中的if else -------')

print([x if x % 2 == 0 else -x for x in range(1, 10)])

print('------- if 在for 前才有else, for后是过滤 不要else -------')

print('------- practise -------')

L = ['Hello', 'World', 18, 'Apple', None]

# print([s.lower() for s in L])

L2 = [i.lower() for i in L if isinstance(i, str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')