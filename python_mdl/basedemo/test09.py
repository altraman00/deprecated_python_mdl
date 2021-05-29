#!/usr/bin/python3

listStr = [(123, 1), (345, 3), (434, 2)]


# 根据元组的第几个元素正序倒叙排列
def getSecondVal(str):
    return str[0]


listStr.sort(key=getSecondVal, reverse=True)

print('sort:', listStr)
