from django.shortcuts import render
from news.models import NewsPostModel ,News_Category

def home(req):
    all_news = NewsPostModel.objects.all()
    return render(req,'news/index.html',{"all_news":all_news})


def News_Category_View(req , slug):
    n_c_v = News_Category.objects.filter(category_slug=slug)
    return render(req,"news/category.html",{"c_news":n_c_v})



def news_detail(req,slug):
    my_news = NewsPostModel.objects.filter(news_slug=slug)
    return render(req,"news/detail.html",{"my_news":my_news})