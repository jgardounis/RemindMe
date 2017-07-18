from django import forms
from django.forms import ModelForm, TextInput, ChoiceField, Select
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
import datetime

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
	catname_text = forms.CharField(max_length=200)
	catdesc_text = forms.CharField(widget=forms.Textarea, max_length=200, required=False, help_text="Use puns liberally")
	created_date = forms.DateField(input_formats=['%d/%m/%Y'], initial=datetime.datetime.now)
		
	def __init__(self, *args, **kwargs):
		super(CategoryForm, self).__init__(*args, **kwargs)
		self.fields['catname_text'].label = "Name"
		self.fields['catdesc_text'].label = "Description"
	
	def clean(self):
		cleaned_data = self.cleaned_data
		catname = cleaned_data.get("catname_text")
		catdesc = cleaned_data.get("catdesc_text")
		
		if catname and catdesc and "Birthdays" in catname:
			raise forms.ValidationError("OOh, Birthdays!!! I'd love me some cake")
		#	msg="OOh, Birthdays!!! I'd love me some cake"
			#self.add_error('catname_text', msg)
			#raise forms.ValidationError(msg)
		#else:	
		return self.cleaned_data
		
	class Meta:
		model = Category
		fields = ('catname_text', 'catdesc_text', 'created_date')
		#labels = {
		#	'catname_text': _('Name'), 'catdesc_text': _('Desc.'),
		#	}
		exclude = ('created_date',)
		widgets = {
			'catdesc_text': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
			}