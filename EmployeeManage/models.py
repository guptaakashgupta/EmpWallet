from django.db import models
from simple_history.models import HistoricalRecords
# Create your models here.

class Employee(models.Model):
	employeeID=models.CharField(max_length=250)
	balance=models.IntegerField()
	history = HistoricalRecords()	
	def __str__(self):
		return "{0} and his wallet balance is  {1}".format(self.employeeID,self.balance)

class Transcation(models.Model):
	time=models.DateTimeField(auto_now_add=True)
	description=models.CharField(max_length=500)
	employeeID=models.ForeignKey(Employee)
	valueOfTranscation=models.IntegerField()
	status=models.CharField(max_length=1,default='created')
	history = HistoricalRecords()
	
	def __str__(self):
		return "{0}    {1}     {2}    {3}    {4}".format(self.time,self.employeeID,self.description,self.valueOfTranscation,self.status)

		
