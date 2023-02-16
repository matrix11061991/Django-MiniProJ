from django.urls import path
from .views import *

urlpatterns = [
	path('account', f_account, name = "account"),
	path('', f_signup, name='signup'),
	path('signin', f_signin, name='signin'),
]