from __future__ import unicode_literals

from datetime import date
from dateutil.relativedelta import relativedelta

from django.contrib.auth.models import User

from django.db import models

# Create your models here.
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

	def approve():
		self.status='approved'
		self.save()

class Employee(models.Model) :

	user=models.OneToOneField(User, on_delete=models.CASCADE)
	start_date=models.DateField()
	days_remain=models.IntegerField(default=18)

	LEAVE_DAYS_PER_YEAR=18
	MAXIMUM_ACCUMULATED_DAYS=5

	##admittedly, this logic should not all reside here, but this is a test with limited time on my side!!
	def save(self, start_date, end_date, *args, **kwargs) :



		leave = self.start_leave(start_date, end_date)

		# work out logic for 18 days, 3 months and carry over here.
		leave_days_available=self.days_remain

		three_months_ago = date.today() - relativedelta(months=3)
		if(self.start_date.date() < three_months_ago) :
			raise ValueError("Your start date is less than 3 months ago.")

		total_leave_taken = Leave.objects.filter(employee=self) ##ideally should be a method in Leave model

		##associated logical error. assumes 5 days accumulated for part of year worked.
		months_formula=12
		total_can_be_taken=self.LEAVE_DAYS_PER_YEAR
		if(self.start_date() > twelve_months_ago) :
			months_formula=24
			total_can_be_taken=self.LEAVE_DAYS_PER_YEAR+self.MAXIMUM_ACCUMULATED_DAYS

		months_formula = date.today() - relativedelta(months=months_formula)

		total_leave_taken = Employee.objects.filter(status='approved').filter(employee=self).filter(start_date__gte=months_formula).aggregate(leave_days=Sum('days_of_leave'))
		
		if total_leave_taken['days_of_leave'] != None :
			leave_days_available=total_can_be_taken-total_leave_taken['days_of_leave']

		if leave_days_available < 1 :
			raise ValueError("You have exhausted all your leave days.")

		leave.approve()

		self.days_remain=leave_days_available
		super(Employee, self).save(*args, **kwargs)

	##workout the weekday calcultation
	def get_num_days(start_date, end_date) :

		num_days = end_date-start_date
		return num_days

	def start_leave(start_date, end_date, number_of_days):
		leave_item=Leave()
		leave_item.employee=self
		leave_item.start_date=start_date
		leave_item.end_date=end_date
		leave_item.days_of_leave=self.get_num_days(start_date, end_date)
		leave_item.status='new'
		leave_item.save()

		return leave_item




