from django.urls import path
from news import views

urlpatterns = [
    path("", views.home),
    path("<slug>/",views.news_detail),
    path("category/<slug>",views.News_Category_View)
]
