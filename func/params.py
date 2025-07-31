
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
  print('name:', name, 'age:', age, 'others:', kw)

print('指定限制的可变参数', person('mm', 12, city='nb', gender='nan'))

print('如何定义中已经有一个可变参数，后面就不需要一个特殊分隔符*了')


print('--------- 6. 参数组合 -----------')

print('必选参数、默认参数、可变参数、命名关键字参数和关键字参数, 组合使用，定义顺序必须是这样')
