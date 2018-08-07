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

## 查询集
`all()`:查询所有

`filter()`:查询满足条件的结果

`exclude()`:获取不满足条件的结果

`order_by()`:排序

`values()`:一个对象构成一个字典，然后构成一个列表返回

## 单个值
`get()`:返回单个满足条件的对象，如果没找到或者找到多条，会抛出异常

`count()`:返回当前查询的总条数

`first()`:返回第一个对象

`last()`:返回最后一个对象

`exists()`:判断查询集中是否有数据，如果有返回True

## 限制查询集
查询集返回列表，可以使用下标的方式进行限制，等同于sql中的limit和offset子句

注意：不支持负数索引，使用下标返回一个新的查询集，不会立即执行查询

## 字段查询
语法：`属性名称__比较运算符=值`
两个下划线左边是属性名称，右侧是比较类型
对于外键，使用`属性名_id`作为外键的原始值
### 比较运算符
* exact:判断相等，大小写敏感，默认表示判等
* contains:是否包含
* startswith,endswith:以value开头或结尾
* isnull,isnotnull:是否为null
* 在前面加一个`i`，表示不区分大小写
* in：是否包含在范围内
* gt,gte,lt,lte:大于，大于等于，小于，小于等于
* year,month,day,week_day,hour,minute,second:对日期某一部分进行运算
* `pk`表示是`Primary Key`,默认主键是`id`
* 跨关联关系的查询：处理join查询
> 语法：`模型类名<属性名><比较>`
> 注：可以没有__<比较>部分，表示等于，结果等同于`inner join`