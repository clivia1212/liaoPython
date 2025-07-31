
age = 20

if age >= 18:
    print('your age is', age)
    print('adult')
elif age >=6:
    print('child')
else:
    print('teen')


# if x: x 非零数值 非空字符串 非空list 就为True

# input str 转 int

str = input('please input your age:')

changed = int(str)

if changed >= 18:
    print('wa kaka')
else:
    print('so younger')

print('------------------------- practice --------------------------------')

# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
# 用if-elif判断并打印结果：

heightStr = input('请输入你的身高(m)：')

weightStr = input('请输入你的体重(kg)：')

height = float(heightStr)
weight = float(weightStr)
# height = 1.75
# weight = 80.5

bmi = weight / (height * height)
prefix = '体重'

if bmi < 18.5:
    print(prefix, '过轻')
elif bmi < 25:
    print(prefix, '正常')
elif bmi < 28:
    print(prefix, '过重')
elif bmi < 32:
    print(prefix, '肥胖')
else:
    print(prefix, '严重肥胖')