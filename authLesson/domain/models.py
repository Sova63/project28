from django.db import models
from .views import *


# Create your models here.
class User(models.Model):
	user_id = models.AutoField(primary_key = True)
	username = models.CharField(max_length=120)
	password = models.TextField()
	user_email = models.CharField(max_length=120)


	def __str__(self):
		return self.username

	def isUserPasswordValid(self,password):
		return decrypt_password(self.password) == password