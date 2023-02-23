from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.db.models import Q

# Create your views here.
def f_signup(request):
	error, message = False, ""
	if request.method == "POST":
		username = request.POST.get('username', None)
		first_name = request.POST.get('firstname', None)
		email = request.POST.get('useremail', None)
		password = request.POST.get('password', None)

		try:
		 	validate_email(email)
		except:
			error, message = True, "Entrer un email valide !!!"
		
		user = User.objects.filter(Q(email = email) | Q(username = username)).first()

		if user:
			error = True
			message = "email ou pseudo existant !!!!"

		if error == False:
			print("success")
			user = User(
				username = username,
				email = email,
				first_name = first_name,
				)
			user.save()
	context = {
		'error': error,
		'message': message,
	}
	return render(request,"accounts/v_signup.html", context)

@login_required(login_url='signin')
def f_account(request):
	return render(request,"accounts/v_account.html")

def f_signin(request):
	if request.method == "POST":
		email = request.POST.get('useremail', None)
		password = request.POST.get('password', None)

		user = User.objects.filter(email = email).first()
		
		if user:
			auth_user = authenticate(username = user.username, password = password)
			if auth_user:
				login(request,auth_user)

				return redirect('account')
			else:
				print("mdp incorrect")
		else:
			print("user not exist")

	return render(request,"accounts/v_signin.html")



def logout(request):
	logout(request)
