# A_Simple_Flask_API

一个简单的Flask与Sklearn结合的API

### 各个文件说明

static/css文件里面主要是HTML页面的各种格式

templates文件夹里面包含两个HTML页面:
  index.html代表app.py程序执行的HTML页面，主要是以文件上传计算的方式
  index_1.html代表app_1.py程序执行的HTML页面，主要是以键盘输入的计算方式
  
model.py表示机器学习训练的文件，最终并保存为model.pkl文件

sales.csv表示model.py中用到的训练数据

app.py和app_1.py表示flask主程序
