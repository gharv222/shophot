from django.db import models

# Create your models here.



class account(models.Model):
	user_name = models.CharField(primary_key=True, max_length=255, null=False)
	nickname = models.CharField(max_length=255, null=False)
	password = models.CharField(max_length=255, null=False)
	email = models.CharField(max_length=255, null=False)

class product_post(models.Model):
	entry_number = models.AutoField(primary_key=True, null=False)
	user = models.CharField(max_length=255, null=False) 	
	product_name = models.CharField(max_length= 255, null=False)
	product_price = models.FloatField(null=False)
	product_store = models.CharField(max_length=255, null=False)
	product_link = models.CharField(max_length=255)
	comment = models.CharField(max_length = 255)
	post_date = models.DateField()


