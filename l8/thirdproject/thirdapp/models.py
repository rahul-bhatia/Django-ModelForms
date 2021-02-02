from django.db import models

# Create your models here.
class WnModel(models.Model):
	name=models.CharField(max_length=20)
	options=models.CharField(max_length=10)
	wn_d=models.DateField(auto_now_add=True)
	wn_t=models.TimeField(auto_now_add=True)

	#to change the name of the default table
	class meta:
		db_table= "Wn_table"