from django.urls import path
from blog.views import *

urlpatterns = [
    path('', f_blog, name='index'),
]