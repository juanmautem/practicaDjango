from django.db import models

# Create your models here.

class userPass(models.Model):
	#campos
	user = models.CharField(max_length = 15)
	password = models.CharField(max_length = 32)
