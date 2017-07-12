from django import forms
from django.forms import ModelForm, Textarea
from django.utils.translation import ugettext_lazy as _

from .models import Reminder, Category

class ReminderForm(forms.ModelForm):
	#category = forms.ForeignKey(Category)
	remtitle_text = forms.CharField(max_length=200)
	remdesc_text = forms.CharField(max_length=200, required=False, help_text="Use puns liberally")
	rem_date = forms.DateField(input_formats=['%d-%m-%Y'])
	#created_date = forms.DateField(input_formats=['%d-%m-%Y'])
	

	class Meta:
		model = Reminder
		#fields = ('remtitle_text', 'remdesc_text', 'rem_date', 'category',)
		exclude = ('created_date',)
		

class CategoryForm(forms.ModelForm):
	catname_text = forms.CharField(label='Name')
	catdesc_text = forms.CharField(max_length=200, required=False, help_text="Use puns liberally")
	created_date = forms.DateField(input_formats=['%d-%m-%Y'])

	#def __init__(self, *args, **kwargs):
		#super(CategoryForm, self).__init__(*args, **kwargs)
		#self.fields['catname_text'].help_text = "The name of your category"
		#self.fields['catname_text'].label = "Name"
	
	class Meta:
		model = Category
		fields = ('catname_text', 'catdesc_text',)
		labels = {
			'catname_text': 'Name'
			}
		exclude = ('created_date',)
		
		