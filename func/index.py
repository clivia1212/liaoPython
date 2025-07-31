
# func查询 官方文档：https://docs.python.org/3/library/functions.html

# 2. help(abc)

# 调用： 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量

a = abs

a(-43)

print('---------- practice: 请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串  ----------')

n1 = 255
n2 = 1000

print(hex(n1), hex(n2))

# 定义

  ## 关键词 def  函数名 括号 参数 冒号 缩进 函数体

def my_abs(x):
  if not isinstance(x, (int, float)): # 类型检查
    raise TypeError('bad operand type')
  if x < 0:
    return -x
  return x

print(my_abs(-4))

print(my_abs(64))

# 命令执行
# 当前目录 from index import my_abs


# 返回多个值 return x, y

import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, 30)

print(x, y)

r = move(100, 100, 60, 30)

print(r)

print('函数实际返回的是一个tuple, 语法上一个tuple可以省略括号')


print('---------- practice: 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0 的两个解。  ----------')

def quadratic(a, b, c):
  if a == 0:
    raise TypeError('a 不能为0')
  
  x0 = b * b - 4 * a * c

  if x0 < 0:
    raise TypeError('无解哦～')

  x1 = (-b + math.sqrt(x0)) / (2 * a)
  x2 = (-b - math.sqrt(x0)) / (2 * a)

  return x1, x2

# 测试

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')