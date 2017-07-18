import datetime
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
	catname_text = models.CharField(max_length=200)
	catdesc_text = models.TextField(max_length=200, null=True, blank=True)
	created_date = models.DateField(default=timezone.now)
	delete_cat = models.BooleanField(default=0)
	# ...
	def __str__(self):              # __unicode__ on Python 2
		return self.catname_text
		
	def was_created_recently(self):
		return self.created_date >= timezone.now() - datetime.timedelta(days=1)
	was_created_recently.admin_order_field = 'created_date'
	was_created_recently.boolean = True
	was_created_recently.short_description = 'Created recently?'
	
	def get_absolute_url(self):
		return reverse('results', kwargs={'pk': self.pk})

class Reminder(models.Model):
	category = models.ForeignKey(Category)
	remtitle_text = models.CharField(max_length=200)
	remdesc_text = models.TextField(max_length=200, null=True, blank=True, help_text="Use puns liberally")
	rem_date = models.DateField('reminder date')
	created_date = models.DateField(default=timezone.now)
	delete_rem = models.BooleanField(default=0)
	# ...
	def __str__(self):              # __unicode__ on Python 2
		return self.remtitle_text
	
	def was_created_recently(self):
		return self.created_date >= timezone.now() - datetime.timedelta(days=1)
	was_created_recently.admin_order_field = 'created_date'
	was_created_recently.boolean = True
	was_created_recently.short_description = 'Created recently?'
	
	def get_absolute_url(self):
		return reverse('details', kwargs={'pk': self.pk})