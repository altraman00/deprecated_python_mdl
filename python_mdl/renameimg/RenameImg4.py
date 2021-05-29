import os

from PIL import Image

# 检查命名

if __name__ == '__main__':

    oldDirPath = '/Users/knight/Desktop/mobvoi/valid_code/code/code_01'
    # oldDirPath = '/Users/knight/Desktop/mobvoi/valid_code/denoise'
    newDirPath = oldDirPath + '/lable'

    oldDiriFiles = os.listdir(oldDirPath)
    if not os.path.exists(newDirPath):
        os.makedirs(newDirPath)
    for file in oldDiriFiles:
        file_path = os.path.join(oldDirPath, file)
        if not file.endswith("png"):
            continue
        # 预览图片
        oldfilename = file.split(".")[0]

        img = Image.open(file_path)
        img.show()

        # print(oldfilename)

        printName = "旧名字：" + oldfilename + "--->新名字:"
        newName = input(printName)
        if newName != "":
            newfilename = "{}.png".format(newName)
            newFilePathStr = newDirPath + "/" + newfilename
            print(newfilename)
            # print(newFilePathStr)
            # img.close()
            cmd = f"mv {file_path} {newFilePathStr}"
            os.system(cmd)
        else:
            cmd = f"mv {file_path} {newDirPath}"
            os.system(cmd)

        os.system('clear')
