from django.conf.urls import url
from RemindMe.views import reminder_new, reminder_edit, reminder_delete, category_new, category_edit, category_delete#, index


from . import views

app_name = 'reminders'

urlpatterns = [
    url(r'^$', views.index, name='index'),
	#url(r'^$', index.as_view(), name='index'),
	url(r'^(?P<category_id>[0-9]+)/detail/$', views.detail, name='detail'),
	url(r'^category(?P<category_id>[0-9]+)/results/$', views.results, name='results'),
	url(r'^reminder(?P<reminder_id>[0-9]+)/details/$', views.reminder, name='reminder'),
	url(r'^reminder/new/$', reminder_new.as_view(), name='reminder_new'),
	url(r'^reminder(?P<pk>[0-9]+)/edit/$', reminder_edit.as_view(), name='reminder_edit'),
	url(r'^reminder(?P<pk>[0-9]+)/delete/$', reminder_delete.as_view(), name='reminder_delete'),	
	url(r'^category/new/$', category_new.as_view(), name='category_new'),
	url(r'^category(?P<pk>[0-9]+)/edit/$', category_edit.as_view(), name='category_edit'),
	url(r'^category(?P<pk>[0-9]+)/delete/$', category_delete.as_view(), name='category_delete'),
]