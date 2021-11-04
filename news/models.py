from django.db import models
from autoslug import AutoSlugField



class News_Category(models.Model):
    name = models.CharField(max_length=150)
    category_slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name
    

class NewsPostModel(models.Model):
    news_title = models.CharField(max_length=150)
    post_time = models.DateTimeField(auto_now_add=True)
    sub_title = models.CharField(max_length=250)
    news_image = models.ImageField(upload_to="news/",max_length=259)
    news_discription = models.TextField(null=True , blank=True)
    news_slug = AutoSlugField(populate_from='news_title')
    newsCategory = models.ForeignKey(News_Category,on_delete=models.CASCADE,null=True,blank=True)

