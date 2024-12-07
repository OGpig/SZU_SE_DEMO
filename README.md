
SZU 2024 年秋季学期「软件工程」期末大作业，基于 MySQL+Django+bootstarap 实现**本科生竞赛交流平台**。

主要环境：

- PowerDesigner
- MySQL Workbench 8.0 CE
- Python 3.12
- Django 5.2.3
- BootStrap 3.3.7
- Django-simpleui

## 系统功能 :snake:

待补充
## 项目结构 :pencil:

```
待补充
```

## 快速开始 :rocket:

1. 初始化：

   - 克隆本项目 `git clone https://github.com/OGpig/SZU_SE_DEMO`

   - 卸载原依赖 `pip uninstall -y -r requirement.txt`

   - 配置新依赖 `pip install -r requirements.txt`

2. 数据库准备：

   - 打开 MySQL Workbench 服务器，创建本地数据库 `create database django_CCOS`

   - 项目参数修改：打开 settings.py 配置文件，找到 MySQL 自定义参数，修改为你自己的配置

4. 项目启动，进入项目 `django_CCOS` 目录，执行：
   - `python manage.py makemigrations`
   - `python manage.py migrate`
   - `python manage.py runserver`
   
5. 前端访问：http://127.0.0.1:8000

5. 后台访问：http://127.0.0.1:8000/admin
   - 创建管理员：`python manage.py createsuperuser`
   - 自行添加数据项



## 鸣谢 :https://github.com/hewei2001love_letter:

感谢 (https://github.com/hewei2001) 小朋友！


