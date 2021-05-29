


# def funcname(listStr):
#     print(listStr);
#     listStr.append([1,2,3])
#     return listStr;
#
#
# a = [10,20,30]
# na = funcname(a)
#
# print(a)
# print(na)
# print(a)


# def test(str):
#     str += 1
#     return str
#
# val = 9
#
# a = test(val)
# print(val)
# print(a)

# def test(str,ddd):
#     print(str,ddd)
#     return
#
# test('111',"qqq")
# test(ddd = '111',str = "qqq")
#
#
# def test2(str, ddd=0):
#     print(str,ddd)
#     return
#
# test2('111')
# test2(str ="qqq")


# def test3(a,*b):
#     print(a)
#     for i in b:
#         print('---',i)
#
# test3(1,2,3,4,5)



# sum = lambda a,b:a+b;
#
# print(sum(1,2))



# total = 0
#
# print(total)
#
# def sum(a,b):
#     # global total
#     total = a + b
#     return total
#
# sum(1,2)
#
# print(total)


num = 0
def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明
        # global num
        num = 100
        print(num)
    inner()
    print(num)

print('before',num)
outer()
print('after',num)

