from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.models import User
# Create your views here.

from .models import product_post, account


# Create your views here.

def feed(request):
	"""
	Renders the product feed of all product entries
	"""
	post = product_post.objects.all()
	context = {'post': post}

	return render(request, 'feed.html', context)

def home(request):
	"""
	Renders a home page for a specific user
	"""
	current_user = request.user
	context = {'current_user':current_user}
	return render(request, 'shophome.html', context)


def post(request):
	"""
	Renders a a page in which a user can create a post entry that save to the database
	"""
	if request.method == "POST":
		post_ = request.POST

		new_post = product_post(product_name = post_['pro_name'], user = request.user,
					product_price = post_['pro_price'],product_store = post_['pro_store'],
					product_link = post_['pro_link'], comment = post_['pro_comment'], 
					post_date = datetime.now()) 
		new_post.save()

	context = {}

	return render(request, 'post.html', context)


