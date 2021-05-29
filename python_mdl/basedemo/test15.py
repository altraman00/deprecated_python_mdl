table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
    print('{0:10} ==> {1:10d}'.format(name, number))

    print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))

    print('Runoob: {0[Runoob]:3d};Google: {0[Google]:3d};Taobao: {0[Taobao]:3d}'.format(table))