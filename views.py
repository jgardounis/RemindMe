from django.shortcuts import redirect
from django.http import Http404
from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages



# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
#from django.urls import reverse_lazy
from RemindMe.models import Reminder, Category

from .forms import ReminderForm, CategoryForm

from .models import Category, Reminder


#class index(ListView):
#	model = Category
#	template_name = 'remindme/index.html'
	
#	def get_context_data(self, **kwargs):
#		context = super(index, self).get_context_data(**kwargs)
#		latest_category_list = get_list_or_404(Category.objects.order_by('-created_date')[:15])
#		return HttpResponseRedirect(reverse('reminders: index'), args=('latest_category_list'))
		#return context
	
def index(request):
	latest_category_list = Category.objects.all().order_by('-created_date')[:15]
	return render(request, 'remindme/index.html', {'latest_category_list': latest_category_list})

def detail(request, category_id):
	category = get_object_or_404(Category, pk=category_id)
	return render(request, 'remindme/detail.html', {'category': category})

def results(request, category_id):
	category = get_object_or_404(Category, pk=category_id)
	return render(request, 'remindme/results.html', {'category': category})

def reminder(request, reminder_id):
	reminder = get_object_or_404(Reminder, pk=reminder_id)
	#return HttpResponse("You're checking reminder of category %s." % category_id)
	return render(request, 'remindme/remdetail.html', {'reminder': reminder})

class category_new(CreateView):
	model = Category
	#fields = ['catname_text', 'catdesc_text', 'created_date']
	template_name = 'remindme/category_form.html'
	form_class = CategoryForm
	
	def get_success_url(self):
		return reverse_lazy('reminders:results', args=(self.object.pk,))
	
	def form_valid(self, form):
		f = form.save(commit=False)
		f.save()
		return super(category_new, self).form_valid(form)
		#return super(reverse('results', args=[f.id]))
		#return HttpResponseRedirect(reverse('reminders:results', args=(f.id,)))
		#return HttpResponse("Success!")
	
	
class category_edit(UpdateView):
	model = Category
	#fields = ['catname_text', 'catdesc_text', 'created_date']
	template_name = 'remindme/category_edit.html'
	form_class = CategoryForm
	
	def form_valid(self, form):
		f = form.save(commit=False)
		f.save()
		return HttpResponseRedirect(reverse('reminders:results', args=(f.id,)))
		
	def get_object(self):
		object = super(category_edit, self).get_object()
		return object

class category_delete(DeleteView):
	model = Category
	success_url = '/RemindMe/'
	success_message = "Category was deleted successfully."
	
	def delete(self, request, *args, **kwargs):
		messages.success(self.request, self.success_message)
		return super(category_delete, self).delete(request, *args, **kwargs)

		
class reminder_new(CreateView):
	model = Reminder
	fields = ['remtitle_text', 'remdesc_text', 'rem_date', 'category',]
	template_name = 'remindme/reminder_form.html'
	
	#def get(self, request, *args, **kwargs):
	#	form = self.reminder-form(initial=self.initial)
	#	return render(request, self.template_name, {'form':form})
	
	def form_valid(self, form):
		#form = self.ReminderForm(request.POST)
		f = form.save(commit=False)
		#f.rem_date = timezone.now()
		#f.created_date = timezone.now()
		f.save()
		return HttpResponseRedirect(reverse('reminders:reminder', args=(f.id,)))
		

class reminder_edit(UpdateView):
	model = Reminder
	fields = ['remtitle_text', 'remdesc_text', 'rem_date', 'category',]
	template_name = 'remindme/reminder_edit.html'
	#form_class = forms.ReminderForm
	
	def form_valid(self, form):
		#form = self.ReminderForm(request.POST)
		f = form.save(commit=False)
		#f.rem_date = timezone.now()
		#f.created_date = timezone.now()
		f.save()
		return HttpResponseRedirect(reverse('reminders:reminder', args=(f.id,)))
		
	def get_object(self):
		object = super(reminder_edit, self).get_object()
		return object

class reminder_delete(DeleteView):
	model = Reminder
	#fields = ['remtitle_text', 'remdesc_text', 'rem_date', 'category',]
	#template_name = 'remindme/reminder_confirm_delete.html'
	#success_url = reverse_lazy('index')
	success_url = '/RemindMe/'
	success_message = "Reminder was deleted successfully."
	
	#def get_object(self, queryset=None):
	#	object=super(reminder_delete, self).get_object()
	#	return object
	#def delete_success(self):
	#	return HttpResponseRedirect(request, 'remindme/reminder_delete_success.html',)
	def delete(self, request, *args, **kwargs):
		messages.success(self.request, self.success_message)
		return super(reminder_delete, self).delete(request, *args, **kwargs)
	
	