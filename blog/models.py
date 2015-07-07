# -*- coding: utf-8 -*-
from django.db import models
from django.utils.timezone import utc
import datetime

class Post(models.Model):
	title=models.TextField()
	entradeta=models.TextField()
	cos=models.TextField()
	data_crea=models.DateField()
	data_pub=models.DateField()
	
class Link(models.Model):
	post=models.ForeignKey("Post")
	url=models.TextField()
	nom=models.TextField()
	
		