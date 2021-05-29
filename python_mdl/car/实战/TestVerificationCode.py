import requests
import os
import json


def testValidCode():
    # dir_path = '/Users/knight/Desktop/mobvoi/valid_code/code/code_03'
    dir_path = '/Users/knight/Desktop/mobvoi/valid_code/code/test'
    image_paths = os.listdir(dir_path)
    total_count = 0
    right_count = 0
    for i, file_path in enumerate(image_paths):
        total_count += 1
        if file_path.endswith('.png'):
            img_path = os.path.join(dir_path, file_path)
            file_rb = open(img_path, 'rb')
            print(type(file_rb))
            file = {'file': open(img_path, 'rb')}
            user_info = {'name': 'letian'}
            r = requests.post("http://10.27.0.3:8080/ImageUpdate", data=user_info, files=file)
            # r = requests.post("http://172.20.10.6:8080/ImageUpdate", data=user_info, files=file)
            # print(r.content)
            try:
                code = json.loads(r.content)['result']
            except:
                print("解析异常" + img_path)
                pass
            img_name = file_path.split(".")[0]
            valid_right = True if code == img_name else False
            print('识:' + code + '--->标:' + img_name + '--->' + str(valid_right))
            if valid_right:
                right_count += 1

    right_rate = 100 * round(float(right_count) / float(total_count), 2)
    print('总共%d个，成功%d个，成功率: %d%%' % (total_count, right_count, right_rate))


if __name__ == '__main__':
    testValidCode()
