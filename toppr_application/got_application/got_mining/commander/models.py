from __future__ import unicode_literals

from django.db import models

class AttackerCommander(models.Model):
	name=models.CharField(max_length=200,verbose_name="Name")

	def __unicode__(self):
		return self.name


class DefenderCommander(models.Model):
	name=models.CharField(max_length=200,verbose_name="Name")

	def __unicode__(self):
		return self.name

