
# 递归函数：函数内部调用自己

print('----------------阶乘-----------------')


def fact(n):
  if n > 0:
    return n * fact(n - 1)
  return 1

print(fact(5))


print('1. 理论上每一个递归函数都可以用循环实现 2.递归函数过深会栈溢出')

print('缓解办法：1. 尾递归优化')

def fact(n):
  return fact_iter(n, 1)

def fact_iter(num, result):
  if num > 0:
    return fact_iter(num - 1, num * result)
  return result

print(fact(5))


print('-------------- 汉诺塔 -------------')

def move(n, a, b, c):
  if n == 1:
    print(a, '-->', c)
  else:
    move(n - 1, a, c, b)
    move(1, a, b, c)
    move(n - 1, b, a, c)

print(move(3, 'a', 'b', 'c'))
