from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponse, HttpResponseRedirect
# Create your views here.

from .models import product_post, account


# Create your views here.

def feed(request):
	"""
	Renders the product feed of all product entries
	"""
	if (request.user.is_authenticated)==False:
		return HttpResponseRedirect('http://127.0.0.1:8000/authentication_error')
	post = product_post.objects.all()
	context = {'post': post}

	return render(request, 'feed.html', context)

def home(request):
	"""
	Renders a home page for a specific user
	"""
	if (request.user.is_authenticated)==False:
		return HttpResponseRedirect('http://127.0.0.1:8000/authentication_error')
	
	my_posts = product_post.objects.filter(user=request.user)
	context = {'my_posts':my_posts}
	return render(request, 'shophome.html', context)


def post(request):
	"""
	Renders a a page in which a user can create a post entry that save to the database
	"""
	if (request.user.is_authenticated)==False:
		return HttpResponseRedirect('http://127.0.0.1:8000/authentication_error')
	if request.method == "POST":
		post_ = request.POST

		new_post = product_post(fname = request.user.first_name, lname = request.user.last_name, product_name = post_['pro_name'], 
					user = request.user, product_price = post_['pro_price'],product_store = post_['pro_store'],
					product_link = post_['pro_link'], comment = post_['pro_comment'], 
					post_date = datetime.now()) 
		new_post.save()

	context = {}

	return render(request, 'post.html', context)


