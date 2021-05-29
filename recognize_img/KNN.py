# -*-coding:utf-8-*-
import numpy as np
from sklearn import neighbors
import os
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.externals import joblib

import cv2

if __name__ == '__main__':
    # 读入数据
    data = []
    labels = []
    img_dir = './img_train_cut'
    img_name = os.listdir(img_dir)
    # number = ['0','1', '2','3','4','5','6','7','8','9']
    for i in range(len(img_name)):
        path = os.path.join(img_dir, img_name[i])
        # cv2读进来的图片是RGB3维的，转成灰度图，将图片转化成1维
        image = cv2.imread(path)
        im = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = im.reshape(-1)
        data.append(image)
        y_temp = img_name[i][-5]
        labels.append(y_temp)

    # 标签规范化
    y = LabelBinarizer().fit_transform(labels)

    x = np.array(data)
    y = np.array(y)

    # 拆分训练数据与测试数据
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    # 训练KNN分类器
    clf = neighbors.KNeighborsClassifier()
    clf.fit(x_train, y_train)

    # 保存分类器模型
    joblib.dump(clf, './knn.pkl')

    # # 测试结果打印
    pre_y_train = clf.predict(x_train)
    pre_y_test = clf.predict(x_test)
    class_name = ['class0', 'class1', 'class2', 'class3', 'class4', 'class5', 'class6', 'class7', 'class8', 'class9']
    print(classification_report(y_train, pre_y_train, target_names=class_name))
    print(classification_report(y_test, pre_y_test, target_names=class_name))

    # clf = joblib.load('knn.pkl')
    # pre_y_test = clf.predict(x)
    # print pre_y_test
    # print classification_report(y, pre_y_test, target_names=class_name)

