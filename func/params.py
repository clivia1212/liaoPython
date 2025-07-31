
# 除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数

print('--------- 1. 位置参数 -----------')

def power(x):
  return x * x

print('power(5): ', power(5))

print('power(15): ', power(15))

def power(x, n):
  r = 1
  while n > 0:
    n = n - 1
    r = x * r
  return r

# print('power(5): ', power(5))

print('power(5, 2): ', power(5, 2))

print('--------- 2. 默认参数 -----------')

def power(x, n = 2):
  r = 1
  while n > 0:
    n = n - 1
    r = x * r
  return r

print('power(5): ', power(5))

print('power(5, 3): ', power(5, 3))


print('--------- 默认参数1: 必选在前，默认在后 2: 变化大在前，变化小在后 -----------')

def enroll(name, gender):
  print('name = ', name)
  print('gender = ', gender)

print('enroll("Sarah", "F")', enroll('Sarah', 'F'))


def enroll(name, gender, city = 'ningbo', age = 16):
  print('name = ', name)
  print('gender = ', gender)
  print('city = ', city)
  print('age = ', age)

print('enroll("Sarah", "F")', enroll('Sarah', 'F'))

print('--------- 默认参数缺点：要按顺序提供 -----------')

print('--------- 默认参数缺点2：坑 -----------')

def add_end(L =[]):
  L.append('END')
  return L

print('add_end([1,2,3 ]):', add_end([1,2,3 ]))
print('add_end(["x",2,3 ]):', add_end(["x",2,3 ]))

print('add_end():', add_end())
print('add_end():', add_end())

print('--------- 函数定义, L就被计算出来，每次调用，如果改了L内容，下次调用，就不是定义时的[] -----------')
print('--------- 定义默认参数要牢记一点：默认参数必须指向不变对象！ -----------')

def add_end(L = None):
  if L is None:
    L = []
  L.append('END')
  return L

print('--------- 3. 可变参数 * -----------')

print('--------- 给定一组数字a，b，c……，请计算a2 + b2 + c2 + …… -----------')

def calc(numbers):
  r = 1
  for n in numbers:
    r = r + n * n
  return r

print('calc([1,2,3]): ', calc([1,2,3]))
print('calc((1,2,3)): ', calc((1,2,3, 5)))
# print('calc(1, 2, 3, 6): ', calc(1, 2, 3, 6))


def calc(*numbers):
  r = 1
  for n in numbers:
    r = r + n * n
  return r

print('calc(1, 2, 3, 6): ', calc(1, 2, 3, 6))

print('--------- 4. 关键字参数 ** 0个或任意个含参数名的参数 dict -----------')

def person(name, age, **kw):
  print('name:', name, 'age:', age, 'others:', kw)

print('person("Michael", 30)', person('Michael', 30))

print('person("Michael", 30, city="beijing")', person('Michael', 30, city='beijing'))

extra = { 'a': 323, 'fs': 'fdsds' }
print('person("Michael", 30, **extra)', person('Michael', 30, **extra))

print('--------- 5. 命名关键字参数 -----------')

def person(name, age, *, city, gender):
  print('name:', name, 'age:', age, 'city:', city, 'gender:', gender)

print('指定限制的可变参数', person('mm', 12, city='nb', gender='nan'))

print('如何定义中已经有一个可变参数，后面就不需要一个特殊分隔符*了')


print('--------- 6. 参数组合 -----------')

print('必选参数、默认参数、可变参数、命名关键字参数和关键字参数, 组合使用，定义顺序必须是这样')


def f1(a, b, c=0, *args, **kw):
  print('a = ', a, 'b = ', b, 'c = ', c, 'args = ', args, 'kw = ', kw)

def f2(a, b, c=0, *, d, **kw):
  print('a = ', a, 'b = ', b, 'c = ', c, 'd = ', d, 'kw = ', kw)

f1(1, 2)
f1(1, 2, c=3)
f1(1,2,3,'a', 'b')
f1(1,2,3,'a', 'b', x=99)
f2(1,2,d=99,ext=None)

print('------神奇的是通过一个tuple和dict就能调用------')

args = (1, 2, 3,4)
kw = {'d':33, 'x': 'dfs'}
f1(*args, **kw)

print('------practice------')

print('1.以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：')

def mul(x, y):
  return x * y

def mul(x, *args):
  m = x
  for y in args:
    m = m * y
  return m

print('mul(3)', mul(3))

print('mul(3, 4, 5)', mul(3, 4, 5))


#测试
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
  print('mul(5)测试失败!')
elif mul(5, 6) != 30:
  print('mul(5, 6)测试失败!')
elif mul(5, 6, 7) != 210:
  print('mul(5, 6, 7)测试失败!')
elif mul(5, 6, 7, 9) != 1890:
  print('mul(5, 6, 7, 9)测试失败!')
else:
  try:
    mul()
    print('mul()测试失败!')
  except TypeError:
    print('测试成功')


print('--------小结--------')

print('''
1. 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
2. *args 是可变参数，args接收的是一个tuple
3. **kw 是关键字参数，kw接收的是一个dict
4. 可变参数既可以直接传入： func(1, 2, 3) ，又可以先组装list或tuple，再通过 *args 传入：
func(*(1, 2, 3))
5. 关键字参数既可以直接传入： func(a=1, b=2) ，又可以先组装dict，再通过 **kw 传入：
func(**{'a': 1, 'b': 2}) 。 
6. 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
7. 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符 * ，否则定义的将是位置参
数
''')