from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.db import models

# Create your models here.
class Leave(models.Model) :

	STATUS_CHOICES = (
		('new', 'New'),
		('approved', 'Approved'),
		('declined', 'Declined')
	)

	employee=models.ForeignKey(Employee)
	start_date=models.DateField()
	end_date=models.DateField()
	days_of_leave=models.IntegerField()
	status=models.CharField(choices=STATUS_CHOICES, default='new')

class Employee(models) :

	user=models.OneToOneField(User, on_delete=models.CASCADE)
	start_date=models.DateField()
	days_remain=models.IntegerField()

	def save(self, *args, **kwargs) :
		pass
		# work out logic for 18 days, 3 months and carry over here.
		# if not self.days_remain :

			# if start_date 

