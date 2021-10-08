## 使用 admin 初始化空项目

~~~~~~

mydjangoadmin # 项目名

django-admin startproject mydjangoadmin

~~~~~~


* 修改 settings.py文件 修改数据库 、 修改时钟
* djangoadmin 必须是空的
~~~~~~

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangoadmin',
        'USER':'root',
        'PASSWORD':'root',
        'HOST':'127.0.0.1',
        'PORT':4306,
    }
}
TIME_ZONE = 'Asia/Shanghai'
LANGUAGE_CODE = 'zh-Hans'
~~~~~~


* 初始化

~~~~~~
python3 manage.py migrate

~~~~~~


* 创建admin
~~~~~~

python3 manage.py createsuperuser

~~~~~~

* 运行

~~~~~~
python3 manage.py runserver 0.0.0.0:7890
~~~~~~

* git clone 后注意添加 models 

~~~~~~
python3 manage.py makemigrations --empty mydjangoadmin 
python3 manage.py makemigrations
python3 manage.py migrate
~~~~~~

* 管理员访问地址

~~~~~~
http://ip:port/admin/ 
~~~~~~


* 项目探针 

~~~~~~
http://ip:port/ping/
http://ip:port/check/
~~~~~~

* settings.py 配置输出日志
* 使用方在 views.py 有使用

* 直接拉取项目需要初始化一下 sql 文件中的 sql

* 用户

|登录账号|登录密码|备注|
|----|----|----|
|admin| admin |管理员|

