
# 函数式编程：高度抽象的编程范式

# 高阶函数 （一个函数接收另一个函数作为参数）

# 变量可以指向函数

# 函数名也是变量


def add(x, y, f):
  return f(x) + f(y)


print(add(-5, 6, abs))

# map/reduce

# map: 将一个函数作用于一个序列，以此得到另一个序列

# reduce: 将一个函数依次作用于上次计算的结果和序列的下一个元素，以此得到最终结果

def f(x):
  return x * x

r = map(f, range(10))

print(list(r))

print('------ reduce --------')

from functools import reduce
def add(x, y):
  return x + y

print(reduce(add, [1, 3, 5, 7, 9]))

def fn(x, y):
  return x * 10 + y

print(reduce(fn, [1, 3, 5, 7, 9]))

print('------ map str 转 int -----')

def char2num(s):
  digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9 }
  return digits[s]

print(reduce(fn, map(char2num, '12123')))

# str2int 函数

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9 }

def str2int(s):
  def fn(x, y):
    return x * 10 + y
  
  def char2num(s):
    return DIGITS[s]
  
  return reduce(fn, map(char2num, s))

# lambda 函数简化

def str2int(s):
  return reduce(lambda x, y: x * 10 + y, map(char2num, s))

print('---------- practice ---------')


print('---------- 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：["adam", "LISA", "barT"]，输出：["Adam", "Lisa", "Bart"] -------------')


def normalize(name):
    def toLower(s):
      return s.lower()

    nL = list(map(toLower, name))
    nL[0] = nL[0].upper()
    new_name = ''
    for x in nL:
      new_name = new_name + x
    return new_name


# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

print('---------- 请编写一个prod()函数，可以接受一个list并利用reduce()求积 -------------')

from functools import reduce

def prod(L):
  def fn(x, y):
    return x * y
  return reduce(fn, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


print('---------- 利用map和reduce编写一个str2float函数，把字符串"123.456"转换成浮点数123.456 -------------')

from functools import reduce

# def fn2(x, y):
#   return x * 0.1 + y

def str2float(s):
  def char2num(s):
    return DIGITS[s] if s in DIGITS else s

  is_integer = True
  decimal_wight = 1

  def combine(x, y):
    nonlocal is_integer, decimal_wight

    if y == '.':
      is_integer = False
      return x
    if is_integer:
      return x * 10 + y
    else:
      decimal_wight *= 0.1
      return x + y * decimal_wight
  
  return reduce(combine, map(char2num, s))

    
  

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')


print('------------------ filter --------------')

def is_odd(x):
  return x % 2 == 1

print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7])))

def not_empty(s):
  return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

# 奇数生成器
def _odd_iter():
  n = 1
  while True:
    n += 2
    yield n

# 有余数
def _not_divisible(n):
  return lambda x: x % n > 0

# 素数生成器
def primes():
  yield 2
  it = _odd_iter()
  while True:
    n = next(it)
    yield n
    it = filter(_not_divisible(n), it) #过滤n的倍数

for n in primes():
  if n < 100:
    print(n)
  else:
    break

print('-------------- practice 回数是指从左向右读和从右向左读都是一样的数--------------')

def is_palindrome(n):
  s = str(n)
  l = len(s)
  for i in range(l // 2):
    if s[i] != s[-(i + 1)]:
      return False
  return True

def is_palindrome(n):
  s = str(n)
  return s[:] == s[::-1]

# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')