def getText():
    txt = open('/Users/knight/Desktop/test/shashibiya.txt', 'r').read()
    txt = txt.lower()   # 去掉大小写干扰
    # 去掉特殊符号干扰
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\'':
        txt = txt.replace(ch, ' ')
    return txt

hamletTxt = getText()
words = hamletTxt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
# 将其按照词出现数量按照降序排列
items.sort(key = lambda x : x[1], reverse = True)

for i in range(20):
    word, count = items[i]
    print('{:^10}{:^10}'.format(word, count))
