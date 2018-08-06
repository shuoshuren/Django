# Django

## test1
## 创建项目
`django-admin startproject test1`

## 创建App
`django-admin startapp booktest`

## 生成迁移
`python manage.py makemigrations`

## 迁移
`python manage.py migrate`

## 启动服务
`python manage.py runserver 8080`

## 创建管理员
`python manage.py createsuperuser`

## test2
## 使用数据库生成模型类
`python manage.py` inspectdb > booktest/models.py

## python3 mysql Driver
`pip install mysqlclient`