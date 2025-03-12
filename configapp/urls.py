from django.urls import path

from .views import *

urlpatterns = [
    path('index/',index, name='index'),
    path('categories/<int:category_id>',categories,name='categories'),
    path('new_about/<int:new_id>',new_about,name='new_about'),
    path('add_news/',add_news,name='add_news'),
    path('update_new/<int:new_id>',update_news,name='update_new'),
    path('add_category/',add_categories,name='add_categories'),
    # path('', index, name='home'),
    path('',LoginPage, name='Login'),
    path("search-news/", search_news, name="search-news"),
]
