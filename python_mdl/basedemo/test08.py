#!/usr/bin/python3

listStr = [123, 443, 3213]

seq = (3, 4, 5)

print(listStr)

# del list[1]

# print('after del :', list)

print('max', max(listStr))
print('min', min(listStr))
print('len', len(listStr))

seq2 = list(seq)
print('tuple-->list:', seq2)

seq2.append(6)

print('seq2:', seq2)

print('count:', listStr.count(seq2))

listStr.insert(0, 999)
print('insert:', listStr)

listStr.remove(999)
print('remove:', listStr)

listStr.reverse()
print('reverse:', listStr)

listStr.sort(reverse=True)
print('sort:', listStr)
