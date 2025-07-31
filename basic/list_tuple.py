
# list: 有序的集合

# len() [0] len() - 1 -1

friends = ['pangpang', 'yy', 'hy']

print(f'init friends: {friends}')

print('len(friends): %d' % (len(friends)))

print('len[0]: %s' % (friends[0]))

print('friends[-1]: %s' % (friends[-1]))

friends.append('mm')

print(f'append friends: {friends}')

friends.insert(1, 'haha')

print(f'insert 1 friends: {friends}')

friends.pop()

print(f'pop friends: {friends}')

friends.pop(1)

print(f'pop 1 friends: {friends}')

friends[2] = '2change'

print(f'替换index2: {friends}')

friends[0] = [23, '3434', True]

print(f'list 不同类型: {friends}')

print(f'friends[0][2]: {friends[0][2]}')


print('----------------------------------------------------------------------------------------------------------')

# tuple（元组）: 有序列表

# 特点：一旦初始化不能修改；没有append inset 赋值  => 代码更安全

tuple = ('pp', 'yy', 'mm', [1, 3])
print(f'init tuple: {tuple}')


print(f'tuple[1]: {tuple[1]}')

print(f'tuple[-1]: {tuple[-1]}')

# 数字1 和 tuple 1 元素 歧义
tuple1 = (1)
realTuple1 = (1,)

print(f'tuple(1) 和 tuple(1,) {tuple1} 和 {realTuple1}')

# 指向不变
tuple[3][0] = 'x'
tuple[3][1] = 'xdfsd'


print(f'change tuple list: {tuple}')


print('----------------------------------------------------------------------------------------------------------')

print('practice')

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Bob']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Bob:
print(L[2][2])
