import cv2
import os

if __name__ == '__main__':
    filePath = '/Users/knight/Desktop/mobvoi/valid_code/code/code_02'
    path = filePath + '/lable'
    files = os.listdir(filePath)
    if not os.path.exists(path):
        os.makedirs(path)
    for file in files:
        file_path = os.path.join(filePath, file)
        im = cv2.imread(file_path)
        if not file.endswith("png"):
            continue
        cv2.imshow(file, im)
        key = cv2.waitKey(0)
        char = input("字符：")
        if char != "":
            filename_ts = file.split(".")[0]
            outfile = "{}.png".format(char)
            outpath = os.path.join(path, outfile)
            cv2.imwrite(outpath, im)
        cmd = f"mv {file_path} {newFilePathStr}"
        os.system(cmd)
