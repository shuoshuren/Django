# Django

## 概述
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

## Model
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

### 聚合函数
> 使用`aggregate()`函数返回聚合函数的值
> 函数：Avg,Count,Max,Min,Sum

### F对象(django.db.models.F)
* 可以使用模型的字段A和字段B进行比较，如果A写在等号左边，B出现在等号的右边，需要通过F对象构造 `list.filter(bread__gte=F('bcomment'))`
* django 支持对F对象进行算数运算
* F()对象还可以写作“模型类__列名”进行关联查询 `list.filter(isDelete=F('heroinfo__isDelete'))`
* 对于data/time字段，可与`timedelta()`进行运算

### Q对象(django.db.models.Q)
* 过滤器的方法中关键字参数查询，会合并为`and`进行
* 需要进行`or`查询，使用`Q()`对象
* Q对象可以使用'&(and)、|(or)'操作符组合
* 当操作符应用在两个Q对象时，会产生一个新的Q对象
* 使用`~(not)`操作付在Q对象前表示取反
* 过滤器函数可以传递多个Q对象作为位置参数，如果有多个，这些参数的逻辑为and
* 过滤器函数可以混合使用Q对象和关键字参数，所有的参数将and在一起，Q对象必须位于关键字参数的前面

## View
### URLconf
* 正则表达式非命名组，通过位置参数传递给视图
`re_path(r'^([0-9]+)/$',views.detail,name='detail)`
* 正则表达式命名组，通过关键字参数传递给视图
`re_path(r'^(?P<id>[0-9]+)/$',views.detail,name='detail')`
* 参数匹配规则：优先使用命名参数，如果没有命名参数则使用位置参数，捕获的参数作为字符串传递给视图

### Request
> * 属性
* path:表示请求的页面完整路径，不包含域名
* method:表示请求的HTTP方法
* encoding:一个字符串，表示请求的数据的编码方式
* GET:一个类似字典的对象，包含get请求方式的所有参数
* POST:一个类似字典的对象，包含post请求方式的所有参数
* FILES:一个类似字典的对象，包含所有上传文件
* COOKIES: 一个字典，包含所有cookie,键和值都为字符串
* session:一个可读写的字典对象，表示当前回话，当django启用支持时，才可用

> * 方法
* is_ajax():如果请求是通过XMLHttpRequest发起，则返回true

### QueryDict对象
* request对象属性GET,POST都是QueryDict对象
* get():根据键获取值，如果一个键有多个值，则获取最后一个
`dict.get('键',default)`或简写为`dict['键']`
* getlist():根据键获取值，将键的值以列表返回，可以获取一个键多个值
`dict.getlist('键',default)`



















