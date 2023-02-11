from django.shortcuts import render

# Create your views here.
def f_blog(request):
	return render(request,"blog/v_blog.html")