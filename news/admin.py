from django.contrib import admin
from news.models import News
# Register your models here.

#admin.site.register(News)
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','created_at', 'catagory')
    list_filter = ('catagory',)
    date_hierarchy = ('created_at')
