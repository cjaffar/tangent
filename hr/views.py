from django.contrib.auth import authenticate, login
from django.views.generic import View

from django.shortcuts import render

from django.http import HttpResponse

from .forms import LoginForm
# Create your views here.

class LoginView(View) :

	def get(self, request, *args, **kwargs) :

		form = LoginForm()
		return render(request, 'hr/login.html', {'form': form})


	def post(self, request, *args, **kwargs) :

		form = LoginForm(request.POST)

		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(username=cd['username'], password=cd['password'])

			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponse('Authenticated successfully')
				else:
					return HttpResponse('Disabled account')

			else:
				return HttpResponse('Invalid login')