*******开发环境与工具******
windows7+pycharm+python27


*******验证码识别***********
download_img.py:爬取网站验证码
pytesser_pre.py:用pytesser方法进行验证码识别，准确度50%左右

cut_image.py:去噪处理后分割图片，用来做训练集、测试集
KNN.py:使用KNN方法训练分类模型，进行验证码识别，准确度99.6%左右
knn.pkl:训练好的KNN模型
recognize_apply.py:用im_train_cut中的图（单个数字）来测试准确率
recognize_final.py:用验证码原图（4个数字）来测试准确率


*******模拟登陆*************
predict_code.py:把训练好的模型封装在一个函数里，直接可以预测，输入是一张验证码，输出是验证码的数字
login.py:模拟登陆