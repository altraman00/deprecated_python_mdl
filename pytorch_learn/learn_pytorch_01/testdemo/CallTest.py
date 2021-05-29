class Person:

    # 初始化对象的时候必须带参数
    def __init__(self, name):
        print('__init__' + ' hello ' + name)

    # 初始化之后的对象，不需要调用方法名就可传参调用
    def __call__(self, name):
        print('__call__' + ' hello ' + name)

    # 必须要实例对象调用方法名才能调用
    def hello(self, name):
        print('hello' + ' hello ' + name)


person = Person('初始化对象的时候传参')
person('对象实例直接传参调用')
person.hello('对象实例调用方法传参调用')
