from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from shop.models import account


def home(request):

	context = {}
	if (request.user.is_authenticated):
		return HttpResponseRedirect('http://127.0.0.1:8000/shop/home')

	if request.method == "POST":
		login_data = request.POST
		user = authenticate(username=login_data['username'], password=login_data['password'])
		if user is not None:	
			login(request, user)
			return HttpResponseRedirect('http://127.0.0.1:8000/shop/home')		
			
		else:
			return HttpResponseRedirect('http://127.0.0.1:8000/home')



			
				
	return render(request, 'home.html', context)

def signout(request):	
	logout(request)
	context = {}
	return HttpResponseRedirect('http://127.0.0.1:8000/home')

def new_account(request):
	"""
	Creates a new account, saves infor to account table in database
	"""
	user_exists = ''
	fill_in = ''

	if request.method == "POST":
		user = request.POST
		for item in user:
			if user[item] == '':
				fill_in = 'All fields are Required!'
				context = {'user_exists':user_exists, 'fill_in':fill_in}
				return render(request, 'new_account.html', context)
		if User.objects.filter(username=user['username']).exists():
			user_exists = 'UserName ' + user['username'] + ' already exists'			
		else:
			new_user = User.objects.create_user(user['username'], 
				user['email'], user['password'])
			new_user.last_name = user['lname']
			new_user.first_name = user['fname']
			new_user.save()
			return HttpResponseRedirect('http://127.0.0.1:8000/home')			

	context = {'user_exists':user_exists, 'fill_in':fill_in}
	
	return render(request, 'new_account.html', context)

def error(request):
	"""
	dsiplays a page informing user they must be logged in 
	"""
	context = {}
	return render(request,'error.html', context)

