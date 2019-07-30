from django.contrib import admin
from news.models import News, Comment
# Register your models here.

#admin.site.register(News)
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','created_at', 'category')
    list_filter = ('category',)
    date_hierarchy = ('created_at')



@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('news','created_at','updated_at','feedback')
    date_hierarchy = ('created_at')