
# 切片

L = ['mm', 'ss', 'pp']

print(L[0:2])

print(L[:2])

# 倒数切片
print(L[-1:])

L = list(range(100))

print(L)

print(L[:10])

# 前10个每两个数取一个
print('L[:10:2]', L[:10:2])

# 每5个取值
print('L[::5]', L[::5])

print('L[:]', L[:])

T = (0, 1, 2, 3, 4, 5)

print(T[:3])

print('ABDCDASS'[:3])

print('--------------- practice: 利用切片操作，实现一个trim()函数，去除字符串首尾的空格 -------------')

def trim(s):
  if s:
    if s[0] == ' ':
      return trim(s[1:])
    elif s[-1] == ' ':
      return trim(s[:-1])
    return s
  return s


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')