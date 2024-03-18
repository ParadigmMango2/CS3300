from django.db import models
from django.urls import reverse



# Create your models here.

class Portfolio(models.Model):
	title = models.CharField(max_length=200)
	contact_email = models.CharField("Contact Email", max_length=200)
	is_active = models.BooleanField()
	about = models.CharField(max_length=5000, blank = True)

	# Override the string/name function
	def __str__(self):
		return self.title

	# Returns the absolute url
	def get_absolute_url(self):
		return reverse('portfolio_detail', args=[str(self.id)])



class Project(models.Model):
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=5000)
	portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, 
				related_name='projects')

	# Override the string/name function
	def __str__(self):
		return self.title

	# Returns the absolute url
	def get_absolute_url(self):
		return reverse('project_detail', args=[str(self.id)])



class Student(models.Model):
	#List of choices for major value in database, human readable name
	MAJOR = (
		('CSCI-BS', 'BS in Computer Science'),
		('CPEN-BS', 'BS in Computer Engineering'),
		('BIGD-BI', 'BI in Game Design and Development'),
		('BICS-BI', 'BI in Computer Science'),
		('BISC-BI', 'BI in Computer Security'),
		('CSCI-BA', 'BA in Computer Science'),
		('DASE-BS', 'BS in Data Analytics and Systems Engineering')
	)

	name = models.CharField(max_length=200)
	email = models.CharField("UCCS Email", max_length=200)
	major = models.CharField(max_length=200, choices=MAJOR)
	portfolio = models.OneToOneField(
		Portfolio,
		on_delete=models.CASCADE,
	)

	# Override the string/name function
	def __str__(self):
		return self.name

	# Returns the absolute url
	def get_absolute_url(self):
		return reverse('student_detail', args=[str(self.id)])
