from django.db import models
import hashlib

# Create your models here.

class userPass(models.Model):
	#campos
	user = models.CharField(max_length = 15)
	password = models.CharField(max_length = 32)
	def __str__(self):
		return "Id: "+ str(self.id) + "| UserName= " + self.user 