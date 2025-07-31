
# dict

names = ['bb', 'yy', 'mm']

scores = [3, 4, 55]

d = { 'bb': 3, 'yy': 4, 'mm': 55 }

print(d['bb'])

# 判断 in get()

print('bb' in d)

print(d.get('bb'))

#pop

d.pop('mm')

# dist       ** key 不可变对象

# 查找 插入速度极快，不会随着key增加而变慢
# 占大量内存，内存浪费多

# list 相反

# 通过key计算位置 哈希算法

print('------------------- set -------------------------')

# 无重复 无序

s = { 1, 2, 3 }

s.add(4)

s.remove(2)

s2 = { 2, 4, 5 }

s & s2

s | s2

print('------------------- 不可变对象 -------------------------')

a = [1, 3, 0, 4]

a.sort()

print(a)

str = 'abc'

str2 = str.replace('b', 'B')

print(str, str2)