from __future__ import unicode_literals

from django.db import models


class Material(models.Model):
	title = models.CharField(max_length=50)
 	title_content = models.TextField(null=True, max_length=6000)
	title_date = models.DateTimeField('date added')
	def __str__(self):
        	return self.title


