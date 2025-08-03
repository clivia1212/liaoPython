# for ... in ...

# 如何判断一个对象是可迭代对象

from collections.abc import Iterable

print(isinstance('abc', Iterable))


# 索引循环，借助enumerate

for i, value in enumerate(['A', 'B', 'C']):
    print('i:', i, 'value:', value)

print('-------- practice --------')

print('请使用迭代查找一个list中最小和最大值，并返回一个tuple：')

def findMinAndMax(L):
    if L == []:
        return None, None
    min = L[0]
    max = L[0]
    for val in L:
        if val < min:
            min = val
        if val > max:
            max = val
    print('min:', min, 'max:', max)
    return min, max

# 测试
if findMinAndMax([]) != (None, None):
 print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
 print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
 print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
 print('测试失败!')
else:
 print('测试成功!')
