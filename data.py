from tkinter import *
import random
import datetime

# 简单输出
print("Hello, World!")

# 输出日期
print(datetime.date.today())

# 设置输出颜色


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(bcolors.WARNING + "警告的颜色字体?" + bcolors.ENDC)

# 生成随机数
print(random.uniform(10, 20))

# 循环和求和
res = 0
for i in range(1, 101):
    res += i
print(res)

# 字符串长度
s = '卧槽00'
print(len(s))

# 排序
l = ['baaa', 'aaab', 'aaba', 'aaaa', 'abaa']
l.sort()
print(l)

# 连接字符串
delimiter = ','
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))

# time模块
if __name__ == '__main__':
    import time
    print(time.ctime(time.time()))
    print(datetime.date.today())
