import os

from PIL import Image

# 校验命名小于4位的图片并重命名

if __name__ == '__main__':

    oldDirPath = '/Users/knight/Desktop/mobvoi/valid_code/test'
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

        if len(oldfilename) < 4:
            img = Image.open(file_path)
            img.show()

            print(oldfilename)
            newName = input("新名字：")
            if newName != "":
                newfilename = "{}.png".format(newName)
                newFilePathStr = newDirPath + "/" + newfilename
                # print(newfilename)
                # print(newFilePathStr)
                img.close()
                cmd = f"mv {file_path} {newFilePathStr}"
                os.system(cmd)
