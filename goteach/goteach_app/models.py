from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError

from .validators import validate_presentation_file

# Create your models here.
class Class(models.Model):
	title = models.CharField(max_length=200)
	start_date = models.DateField()
	ended = models.BooleanField(default=False)
	about = models.CharField(max_length=5000, blank = True)
	game_link = models.CharField(max_length=500, blank = True)
	presentation_file = models.FileField(upload_to="presentations", null=True, blank=True, validators=[validate_presentation_file])

	# Override the string/name function
	def __str__(self):
		return self.title

	# Returns the absolute url
	def get_absolute_url(self):
		return reverse('view_class', args=[str(self.id)])

	def clean(self):
		if not self.title:
			raise ValidationError({'title': 'Title field is required.'})
		
		if not self.start_date:
			raise ValidationError({'start_date': 'Start date field is required.'})
