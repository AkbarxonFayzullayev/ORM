from django.urls import path

from .views import *

urlpatterns = [
    path('index/',index, name='home'),
    path('categories/<int:category_id>',categories,name='categories'),
    path('new_about/<int:new_id>',new_about,name='new_about'),
    # path('', index, name='home'),
]
