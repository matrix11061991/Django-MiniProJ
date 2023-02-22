from django.contrib.auth.models import User
from django.shortcuts import render
from django.core.validators import validate_email
from django.db.models import Q

# Create your views here.
def f_signup(request):
	error = False
	message = ""

	if request.method == "POST":
		username = request.POST.get('username', None)
		email = request.POST.get('useremail', None)
		password = request.POST.get('password', None)

		try:
		 	validate_email(email)
		except:
			error = True
			message = "Entrer un email valide !!!"
		
		user = User.objects.filter(Q(email = email)| Q(username = username)).first()

		if user:
			error = True
			message = "email ou pseudo existant !!!!"
		#print(username)
		if error == False:
			print("success")
			user = User(
				username = username,
				email = email,
				)
			user.save()
	context = {
		'error': error,
		'message': message
	}
	return render(request,"accounts/v_signup.html", context)

def f_account(request):
	return render(request,"accounts/v_account.html")

def f_signin(request):
	return render(request,"accounts/v_signin.html")
