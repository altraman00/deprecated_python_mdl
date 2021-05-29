
f = open("/Users/knight/Desktop/test/NewFile.txt", "r")


str = f.readlines()


print(str)


f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )


str = f.readlines()


print(str)