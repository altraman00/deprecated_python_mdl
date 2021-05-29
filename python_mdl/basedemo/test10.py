#!/usr/bin/python3

listStr = [(123, 1), (345, 3), (234, 2)]



tul_1 = (1, 2, 3)
tul_2 = (11, 12, 13)

tul = tul_1 + tul_2

print('before : ',tul)

ltulList = list(tul)

print('after : ',ltulList)

print('before turn tuple', listStr)

listToTuplStr = tuple(listStr)

print('after turn tuple', listToTuplStr)







