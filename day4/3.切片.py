"""
切片:操作对象其中的一部分操作:字符串,列表,元组都支持切片

序列[开始位置下标:结束为止下标:步长]
    注意: 不包含结束为止下标对应的数据,正负数都可以,
        步长是选取的间隔(每隔多少个字符),正负数均可以,默认为1
"""

str1 = "aksircmw"
print(str1[2:4])
print(str1[2:4:1])
print(str1[2:4:2])
print(str1[2:8:2])
# 特殊写法
print(str1[:5])  # 不写开始默认从0开始
print(str1[2:])  # 不写结束默认选取到结束
print(str1[:])  # 从头选到尾,选取所有

# 负数测试
print(str1[::-1])  # 步长为负数倒叙排列
print(str1[-4:-1])  # -1代表最后一个数据,从后往前数,但是-1为截取的最后位置
# -1   0   1   2   3   4 ...
print('-----')
print(str1[-4:-1:-1])  # 方向冲突(选取方向 和 步长方向 相反)
print(str1[-1:-4:-1])  # 方向合理
