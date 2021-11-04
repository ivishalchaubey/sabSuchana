from django.contrib import admin
from news.models import NewsPostModel , News_Category

class NewsPostAdmin(admin.ModelAdmin):
    list_display = ("news_title","post_time","sub_title","news_image","news_discription","news_slug")

admin.site.register(NewsPostModel,NewsPostAdmin)

# class News_Category_Admin(admin.ModelAdmin):
#     list_display = ('name')

# admin.site.register(News_Category_Admin,News_Category)

admin.site.register(News_Category)