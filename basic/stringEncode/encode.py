# 字符串  字符编码

# 字符编码前因后果 start-------------------------------

# 文本 转 数字  字节

# 美国人 127个字符 ASCII 编码 大小写字母 数字 符号 1个字节

# 中国人 GB2312

# 日文 韩文... 乱码

# Unicode 字符集   --- 计算机内存

# UCS-16 两个字节表示一个字符

# 统一Unicode编码 优点：解决乱码问题 缺点 多1倍存储空间

# UTF-8 编码： 把一个Unicode字符根据不同数字大小编码成1-6个字节        --------- 硬盘或传输

# 字符编码前因后果 end-------------------------------


# python unicode编码 支持多语言
print('包含中文的str')

# 单字符的编码
print(ord('A'))

# 编码转字符
print(chr(25991))

# 'ABC' b'ABC' 后者每个字符只占一个字节

# python 编码 encode bytes

# python 解码 decode bytes

# str 长度
print(len('dsd'))

# bytes 字节数
print(len(b'dsd'))

# 文件开头 UTF-8 编码
#!/usr/bin/env python3             ------- 告诉Linux/OS X系统 这是一个Python可执行程序
# -*- coding: utf-8 -*-            ------- 告诉Python解释器，按照UTF-8编码读取源代码


# 格式化  %     %s %d %f %x
print('Hello %s, your score is %d.' % ('mick', 89))

# 是否补0 和 位数
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

# %s 会把任何数据类型转为字符串

# 转义 %%

# format

# f.string