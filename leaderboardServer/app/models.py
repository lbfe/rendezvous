from django.db import models

class Volunteer(models.Model):
	id = models.AutoField(primary_key=True) 
	name = models.CharField(max_length=30)
	points = models.IntegerField()
	

