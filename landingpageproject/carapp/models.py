from django.db import models

class Car(models.Model):
	car_name = models.CharField(max_length=120)
	car_img = models.URLField()
	maker = models.CharField(max_length=120)
	model = models.CharField(max_length=120)
	about_car = models.TextField()

	def __str__(self):
		return f"{self.maker} {self.model}"
