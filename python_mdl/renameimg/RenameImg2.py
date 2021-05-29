import os

from PIL import Image

# 预览并重命名

if __name__ == '__main__':

    oldDirPath = '/Users/knight/Desktop/mobvoi/valid_code/code/code_05'
    newDirPath = oldDirPath + '/lable'

    oldDiriFiles = os.listdir(oldDirPath)
    if not os.path.exists(newDirPath):
        os.makedirs(newDirPath)
    for idx, file in enumerate(oldDiriFiles):
        file_path = os.path.join(oldDirPath, file)

        # im = cv2.imread(file_path)
        # if not file.endswith("png"):
        #     continue
        # cv2.imshow(file, im)
        # key = cv2.waitKey(3)
        # char = input("字符：")
        # if char != "":
        #     filename_ts = file.split(".")[0]
        #     outfile = "{}.png".format(char)
        #     outpath = os.path.join(newDirPath, outfile)
        #     cv2.imwrite(outpath, im)
        # cmd = f"rm {file_path}"
        # os.system(cmd)

        if not file.endswith("png"):
            continue
        # 预览图片
        img = Image.open(file_path)
        img.show()

        name = str(idx) + "--新名字："
        newName = input(name)
        if newName != "":
            newfilename = "{}.png".format(newName)
            newFilePathStr = newDirPath + "/" + newfilename
            # print(newfilename)
            # print(newFilePathStr)
            img.close()
            cmd = f"mv {file_path} {newFilePathStr}"
            os.system(cmd)
