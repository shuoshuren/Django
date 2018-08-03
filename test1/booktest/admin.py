from django.contrib import admin
from .models import BookInfo, HeroInfo


# Register your models here.

class BookInfoAdmin(admin.ModelAdmin):
    # 展示列表
    list_display = ['id', 'btitle', 'bpub_date']
    # 过滤字段
    list_filter = ['btitle']
    # 搜索字段
    search_fields = ['btitle']
    # 分页
    list_per_page = 10
    # 详情页 字段分组
    fieldsets = [
        ('base', {'fields': ['btitle']}),
        ('super', {'fields': ['bpub_date']})
    ]


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo)
