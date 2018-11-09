from __future__ import unicode_literals

from django.db import models
#from django_mysql.models import ListCharField


class Material(models.Model):
	title = models.CharField(max_length=50)
 	title_content = models.TextField(null=True, max_length=6000)
	title_date = models.DateTimeField('date added')
	def __str__(self):
        	return self.title

class AWS(models.Model):
	title = models.CharField(max_length=50)
	title_content = models.TextField(null=True, max_length=6000)
	title_date = models.DateTimeField('date added')
	def __str__(self):
        	return self.title

class Azure(models.Model):
	title = models.CharField(max_length=50)
	title_content = models.TextField(null=True, max_length=6000)
	title_date = models.DateTimeField('date added')
	def __str__(self):
        	return self.title
	
class Google(models.Model):
	title = models.CharField(max_length=50)
	title_content = models.TextField(null=True, max_length=6000)
	title_date = models.DateTimeField('date added')
	def __str__(self):
        	return self.title
	
class Rackspace(models.Model):
	title = models.CharField(max_length=50)
	title_content = models.TextField(null=True, max_length=6000)
	title_date = models.DateTimeField('date added')
	def __str__(self):
        	return self.title
	
class Contact(models.Model):
	firstname = models.CharField(max_length=50)
	surname = models.CharField(max_length=50)
	emailaddr = models.EmailField(max_length=100)
	comment = models.TextField(null=True, max_length=2000)
	def __str__(self):
        	return self.title

class ContactUs(models.Model):
	firstname = models.CharField(max_length=50)
	surname = models.CharField(max_length=50)
	emailaddr = models.EmailField(max_length=100)
	comment = models.TextField(null=True, max_length=2000)
	def __str__(self):
        	return self.firstname

class Lists(models.Model):
	title = models.CharField(max_length=50)
	title_content = models.TextField(null=True, max_length=1500)
	title_date = models.DateTimeField('date added')
	listno = models.CharField(null=True, max_length=5)
	section = models.CharField(null=True, max_length=100)
	def __str__(self):
        	return self.title

#class Updates(models.Model):
#	title = models.ListCharField(
#		base_field = models.CharField(max_length=30),
#		size = 5,
#		max_length = (5 * 31)
#	)
#	title_date = models.DateTimeField('updated')
#	def __str__(self):
#       	return self.title
