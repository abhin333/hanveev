from django.db import models

# Create your models here.




class tender_register(models.Model):
	title=models.CharField(max_length=100, default='')
	last_date=models.CharField( max_length=100, default='')
	file=models.FileField(upload_to='tenders/')



class careers_register(models.Model):
	opening_details=models.CharField(max_length=100, default='')
	last_date=models.CharField( max_length=100, default='')
	file=models.FileField(upload_to='careers/')



class news_lines(models.Model):
	description=models.CharField(max_length=100, default='')
	