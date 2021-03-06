from django.db import models

# Create your models here.
class BookInfoManager(models.Manager):
    def get_queryset(self):
        return super(BookInfoManager,self).get_queryset().filter(isDelete=False)

    def create(self,btitile,bpub_date):
        b = BookInfo()
        b.btitle = btitile
        b.bpub_date = bpub_date
        b.bread = 0
        b.bcommet = 0
        b.isDelete = False
        return b


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(db_column='pub_date')
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(null=False)
    isDelete = models.BooleanField(default=False)

    # 元选项
    class Meta(object):
        # 修改表的名字，不添加默认是应用名_类名
        db_table='bookinfo'

    # 自定义管理器，默认objects
    '''
    自定义管理器主要用于下面两种情况：
    1.向管理器中添加额外的方法
    2.修改管理器返回的元素查询集：重写get_queryset()方法
    '''
    books = models.Manager()
    books2 = BookInfoManager()

    @classmethod
    def create(cls,btitile,bpub_date):
        b = BookInfo()
        b.btitle = btitile
        b.bpub_date = bpub_date
        b.bread = 0
        b.bcommet = 0
        b.isDelete = False
        return b


class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField(default=True)
    hcontent = models.CharField(max_length=1000)
    isDelete = models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)

