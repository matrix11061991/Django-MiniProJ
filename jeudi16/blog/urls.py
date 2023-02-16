from django.urls import path
from .views import *

urlpatterns = [
	path('', f_blog, name='blog'),
]