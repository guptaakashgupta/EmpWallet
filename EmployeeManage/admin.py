from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from models import Employee,Transcation

class EmployeeAdmin(SimpleHistoryAdmin):
	pass

class TranscationAdmin(SimpleHistoryAdmin):
	exclude=('status',)
	ordering=['-time']
	actions=['make_published']
	
	def make_published(self,request,queryset):
		for transcation in queryset:
			if transcation.status=='created':
				employeeName=transcation.employeeID.employeeID
				print(employeeName)
				value=transcation.valueOfTranscation
				print(value)
				employeeSet=Employee.objects.filter(employeeID=employeeName)
				for employee in employeeSet:
					employee.balance=employee.balance+value
					print(employee.balance)
					employee.save()
				transcation.status='published'
				transcation.save()
	make_published.short_description="Make selected transcation get published"


admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Transcation,TranscationAdmin)
# Register your models here.
