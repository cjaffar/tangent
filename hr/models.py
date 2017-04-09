from __future__ import unicode_literals

from datetime import date
from dateutil import rrule

from dateutil.relativedelta import relativedelta

from django.contrib.auth.models import User

from django.db import models

# Create your models here.
class Employee(models.Model) :

	user=models.OneToOneField(User, on_delete=models.CASCADE)
	start_date=models.DateField()
	days_remain=models.IntegerField(default=18)

class Leave(models.Model) :

	STATUS_CHOICES = (
		('new', 'New'),
		('approved', 'Approved'),
		('declined', 'Declined')
	)

	employee=models.ForeignKey('Employee')
	start_date=models.DateField()
	end_date=models.DateField()
	days_of_leave=models.IntegerField()
	status=models.CharField(max_length=12,choices=STATUS_CHOICES, default='new')

	LEAVE_DAYS_PER_YEAR=18
	MAXIMUM_ACCUMULATED_DAYS=5

	def save(self, *args, **kwargs) :

		number_of_leavedays=self.get_days_of_leave()

		three_months_ago = date.today() - relativedelta(months=3)
		if(self.employee.start_date.date() < three_months_ago) :
			raise ValueError("Your start date is less than 3 months ago.")

		employee_days_taken=self.get_employee_days_taken()
		if (employee_days_taken + number_of_leavedays) > (self.LEAVE_DAYS_PER_YEAR + self.MAXIMUM_ACCUMULATED_DAYS):
			raise ValueError("You have exceeded your number of available leave days.")

		#logic missing here for accumulated leave days
		employee.days_remain = self.LEAVE_DAYS_PER_YEAR - (self.employee.days_remain+number_of_leavedays)
		employee.save()

		self.days_of_leave=number_of_leavedays

		return super(Leave, self).save(*args, **kwargs)


	def approve():
		self.status='approved'
		self.save()

	def get_days_of_leave(self) :

		start_date=self.start_date
		end_date=self.end_date

		if start_date == None or end_date == None :
			raise ValueError("No valid start or end leave date found.")

		days_off = 5, 6

		workdays = [x for x in range(7) if x not in days_off]
		days = rrule.rrule(rrule.DAILY, dtstart=start_date, until=end_date,byweekday=workdays)

		return days.count( )

	def get_employee_days_taken(self) :
		
		months_formula=12
		if(self.start_date() > twelve_months_ago) :
			months_formula=24

		months_formula = date.today() - relativedelta(months=months_formula)

		total_leave_taken = Employee.objects.filter(status='approved').filter(employee=self).filter(start_date__gte=months_formula).aggregate(leave_days=Sum('days_of_leave'))
		
		if total_leave_taken['days_of_leave'] != None :
			return total_leave_taken['days_of_leave']

		return 0