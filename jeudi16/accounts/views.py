from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
def f_signup(request):
	"""
	username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
	"""
	if request.method == "POST":
		username = request.POST.get('username', None)
		useremail = request.POST.get('useremail', None)
		print(username)
	return render(request,"accounts/v_signup.html")

def f_account(request):
	return render(request,"accounts/v_account.html")

def f_signin(request):
	return render(request,"accounts/v_signin.html")