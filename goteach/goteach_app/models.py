from django.db import models
from django.urls import reverse

# Create your models here.
class Class(models.Model):
	title = models.CharField(max_length=200)
	ended = models.BooleanField()
	about = models.CharField(max_length=5000, blank = True)
	game_link = models.CharField(max_length=500, blank = True)

	# Override the string/name function
	def __str__(self):
		return self.title

	# Returns the absolute url
	def get_absolute_url(self):
	 	return '#'
		#return reverse('view_class', args=[str(self.id)])

