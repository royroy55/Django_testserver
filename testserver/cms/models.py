from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Data(models.Model):
	userdata = models.CharField('username', max_length = 255, default = 'NAME')
	whatdata = models.CharField('Datatype', max_length = 255, default = 'DATA')
	datavalue = models.CharField('value', max_length = 255, default = 'DATA')
	#datavalue = models.FloatField('value', default = 0)