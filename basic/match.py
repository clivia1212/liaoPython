
# if else 可读性差 用 match

# 某个学生的成绩只能是A、B、C，用if语句编写如下：

score = 'B'

print('------------------- if else -----------------------')

if score == 'A':
  print('score is A.')
elif score == 'B':
  print('score is B.')
elif score == 'C':
  print('score is C.')
else:
  print('score is invalid.')


# match ----- python 3.10 以上才支持
print('------------------- match -----------------------')

match score:
  case 'A':
    print('score is A.')
  case 'B':
    print('score is B.')
  case 'C':
    print('score is C.')
  case _: # _表示匹配到其他任何情况
    print('score is invalid')

print('------------------- complex match (多个值｜一定范围、匹配后值绑定到变量)-----------------------')

age = 15

match age:
  case x if x < 10:
    print(f'< 10 years old: {x}')
  case 10:
    print('10 years old')
  case _:
    print('not sure')

print('------------------- match list -----------------------')


args = ['gcc', 'hello.py', 'world.c']

# args = ['clean']
# args = ['gcc']


match args:
  case ['gcc']:
    print('gcc: missing source file(s).')
  case ['gcc', file1, *files]:
    print('gcc compile: ' +  file1 + ', ' + ','.join(files))
  case ['clean']:
    print('clean')
  case _:
    print('invalid command')