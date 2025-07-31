
# 两种循环 for in / while

print('------------------------ for in -------------')

names = ['pp', 'yy', 'mm']

for name in names:
    print(name)

print('------------------------ 1-10 求和 -----------------')

sum = 0

for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

print('------------------------ range list -----------------')

print(list(range(5)))

print('------------------------ 1-100 求和 -----------------')

sum2 = 0

for x in range(101):
    sum2 = sum2 + x
print(sum2)


print('------------------------ while 要计算100以内所有奇数之和 -------------')

sum3 = 0
n = 99

while n > 0:
  sum3 = sum3 + n
  n = n - 2

print(sum3)

print('------------------------ practice -------------')

print('------------------------ practice1 请利用循环依次对list中的每个名字打印出Hello, xxx!：------------- ')

L = ['Bart', 'Lisa', 'Adam']

for name in L:
  print('Hello, ' + name + '!')

print('------------------------ break 跳出整个------------- ')

n2 = 0

while n2 < 100:
  n2 = n2 + 1
  if n2 > 10:
    break

print(n2)

print('------------------------ continue 跳出一次------------- ')

n3 = 0

while n3 < 10:
  n3 = n3 + 1
  if n3 % 2 == 0:
    continue
  print(n3)