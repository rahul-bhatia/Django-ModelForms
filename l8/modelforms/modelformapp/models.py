from django.db import models

# Create your models here.
class EnModel(models.Model):
	name=models.CharField(max_length=30)
	email=models.EmailField()
	phone=models.CharField(max_length=10)
	en_dt=models.DateTimeField(auto_now_add=True)

	def ___str___(self):	
		return self.name
