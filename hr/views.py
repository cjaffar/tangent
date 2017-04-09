import datetime

from django.contrib.auth import authenticate, login
from django.views.generic import View,FormView

from django.shortcuts import render,redirect

from django.http import HttpResponse

from .forms import LoginForm,LeaveForm
from .models import Employee
# Create your views here.

class LoginView(View) :

	def get(self, request, *args, **kwargs) :

		if request.user.is_authenticated() :
			return redirect('employee-view')

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
					return redirect('employee-view')
				else:
					return render(request, 'hr/login.html', {'form': form,'reason':'inactive'})

			else:
				return render(request, 'hr/login.html', {'form': form,'reason':'invalid'})

class EmployeeView(FormView) :

	template_name='hr/leave_form.html'
	success_url = '/hr/success/'
	form_class=LeaveForm

	# def get(self, request, *args, **kwargs) :
		
	# 	form=LeaveForm
	# 	return render(request, 'hr/leave_form.html', {'form':form })

	def form_valid(self, form):

		cleaned=form.cleaned_data

		try :
			leave_start_day=int(cleaned['leave_from_day'])
			leave_start_month=int(cleaned['leave_from_month'])
			leave_start_year=int(cleaned['leave_from_year'])

			leave_end_day=int(cleaned['leave_end_day'])
			leave_end_month=int(cleaned['leave_end_month'])
			leave_end_year=int(cleaned['leave_end_year'])
		except:
			return redirect('employee-view')

		start_date=datetime.date(leave_start_year, leave_start_month, leave_start_year)
		end_date=datetime.date(leave_end_year, leave_end_month, leave_end_day)

		try :
			employee = Employee.objects.get(user=self.request.user)
		except:
			employee=Employee(user=self.request.user,start_date=datetime.date(datetime.today()) )
			employee.days_remain=18 ##Eish
			employee.save()

		try :
			leave=Leave()
			leave.employee=employee
			leave.start_date=start_date
			leave.end_date=end_date
			leave.save()
		except  ValueError, e:
			return render(self.request, 'hr/leave_form.html', {'form':form, 'msg' : repr(e) })

		return super(EmployeeView, self).form_valid(form)
