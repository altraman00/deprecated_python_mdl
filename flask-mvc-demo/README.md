# flask-mvc-demo

# pycharm 创建项目时的虚拟环境

参考：

pycharm 已创建好的项目配置虚拟环境 https://cloud.tencent.com/developer/article/1450212

[新手向视频]新版PyCharm创建项目为什么会有问题 https://zhuanlan.zhihu.com/p/32955028

pycharm 在新建项目时，如果选择的是New environment using [virtualenv] 
这种方式会创建一个新的虚拟 python 环境，创建好一个副本，这个新项目之后安装的所有第三方库仅限于这个副本的环境，而不会影响你原本的 python 和其他项目。
此时项目中会多一个venv的文件夹，就是复制的本机安装的python环境的副本，进入Terminal之后，左边也有(venv)的提示符，说明虚拟环境已经创建成功。
如下：
```
(venv) ➜  flask-mvc-demo git:(master) ✗ pwd
/Users/knight/workspace/sourceTree/os_mdl/mdl/python/flask-mvc-demo
(venv) ➜  flask-mvc-demo git:(master) ✗ python --version
Python 3.7.0
```

1、进入项目中使用的虚拟python环境目录

######（如果上面在进入Terminal之后，左边也有(venv)的提示符的情况下，不进入下面的venv目录，使用的也是新的副本环境）
```
cd /Users/knight/workspace/sourceTree/os_mdl/mdl/python/flask-mvc-demo/venv
```

2、查看python版本
```
python --version
显示项目中使用的python环境
```

3、在项目使用的虚拟python环境的版本下安装requirements.txt需要的包
```
pip3 install -r ../app/requirements.txt
```

4、导出需要的包

######（pip3 freeze 导出的依赖发现不全，有文章推荐使用 `pipenv`）
```
pip3 freeze > ../app/requirements.txt

或者 

pip3 freeze --all > ../app/requirements.txt

```

***

## pip和conda批量导出、安装组件(requirements.txt)

原文链接：https://blog.csdn.net/chekongfu/article/details/83187591

1、pip3批量导出包含环境中所有组件的requirements.txt文件

`pip3 freeze > requirements.txt`

2、pip3批量安装requirements.txt文件中包含的组件依赖

`pip3 install -r requirements.txt`

3、conda批量导出包含环境中所有组件的requirements.txt文件

`conda list -e > requirements.txt`

4、conda批量安装requirements.txt文件中包含的组件依赖

`conda install --yes --file requirements.txt`


***

## Anaconda 换源更改镜像，删源


原文链接：https://blog.csdn.net/weixin_40871455/article/details/90071122

换国内源
windows & mac

1、添加清华源：命令行中直接输入以下命令

```
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge 
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
```
 
 
##### 设置搜索时显示通道地址
```
conda config --set show_channel_urls yes
```

注意如果需要pytorch, 还需要添加pytorch的镜像

```
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
```

2、添加中科大源

```
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/bioconda/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/menpo/
conda config --set show_channel_urls yes
```

Linux
将以下配置文件写在~/.condarc文件中 

```vim ~/.condarc```

添加如下命令：

```
channels:
  - https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
  - https://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  - defaults
show_channel_urls: true
```

无论是在 Mac/Linux/Windows 对应目录的 .condarc 里修改也是可以的。

.condarc 以点开头，一般表示 conda 应用程序的配置文件，在用户的根目录 windows：C:\users\username\，linux：/home/username/ 


##### 删源

换回conda的默认源。查看了conda config的文档后，发现直接执行以下命令即可删除非默认的channels。

```conda config --remove-key channels```


***
# mac下anaconda的安装及简单使用

原文链接：https://blog.csdn.net/lq_547762983/article/details/81003528

常用操作命令：

一、环境操作

1.查看环境管理的全部命令帮助：

```conda env -h```

2.查看当前系统下的环境：

```conda info -e```

3.创建环境：

```conda create env_name ```
 
 (env_name)是环境名称,这条命令将会给Biopython创建一个新的环境，位置在Anaconda安装文件的/envs/snowflakes

创建指定python版本的环境：

```conda create env_name python=3.6```

(3.6为python的版本，根据自己的需要更改)

创建包含某些包的环境：

```conda create env_name numpy scipy```

创建指定python版本下包含某些包的环境：
```conda create env_name python=3.6  numpy scipy```

 

激活（进入）某个环境：

新的开发环境会被默认安装在conda目录下envs文件目录下,你可以指定一个其他的路径；

如果没有指定安装python的版本，conda会安装最初安装conda时所装的那个版本的python。

windows:

```activate env_name```

mac:

```source activate env_name```

退出某个环境：

```deactivate env_name```

复制某个环境：

```conda create new_env_name old_env_name```

删除某个环境：

```conda remove env_name```

二、包管理

查看已安装的包：

```conda list```

查看指定环境下的包：

```conda list -n xxx```

查找包：

```conda search xxx```

更新包：

```conda update xxx```

安装包：

```conda install xxx```

```pip install xxx```

指定的安装环境：

```conda install -n env_name xxx```

 
安装anaconda发行版中所有的包:

```conda install anaconda```

卸载包：

```conda remove xxx```

三、管理conda

检查conda版本：

```conda --version```

升级当前版本的conda：

```conda update conda```
