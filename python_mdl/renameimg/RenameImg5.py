import os

# 校验命名小于4位的图片并重命名

if __name__ == '__main__':

    oldDirPath = '/Users/knight/workspace/sourceTree/os_mdl/mdl/python/recognize_img/img'
    newDirPath = oldDirPath + '/lable'

    # 统计转义的个数
    count = 0

    oldDiriFiles = os.listdir(oldDirPath)
    if not os.path.exists(newDirPath):
        os.makedirs(newDirPath)
    for file in oldDiriFiles:
        file_path = os.path.join(oldDirPath, file)
        if not file.endswith("jpg"):
            continue
        # 预览图片
        oldfilename = file.split(".")[0]
        printName = "旧名字：" + oldfilename
        if len(oldfilename) != 4:
            count += 1
            # 单个'可以起到转义的作用，
            # 如果使用cmd = f"mv {file_path} {newDirPath}" 会出现路径中有空格不能执行的情况
            cmd = f"mv '{file_path}' '{newDirPath}'"
            os.system(cmd)
    print("总共移了" + str(count) + "个")
