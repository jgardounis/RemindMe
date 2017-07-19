from django.contrib import admin
import datetime
from django.utils import timezone
# Register your models here.
from .models import Category, Reminder


class CategoryAdmin(admin.ModelAdmin):
	fieldsets=[
	(None,					{'fields': ['catname_text']}),
	('Category details',	{'fields': ['catdesc_text', 'created_date']}),
	('Delete category ?',	{'fields': ['delete_cat'], 'classes': ['collapse']}),
	]
	list_display = ('catname_text', 'created_date')#, 'was_created_recently')	
	list_filter = ['created_date']
	search_fields = ['catname_text']
	
	
class ReminderAdmin(admin.ModelAdmin):
	fieldsets=[
	(None,					{'fields': ['remtitle_text']}),
	('Reminder details',	{'fields': ['remdesc_text', 'rem_date', 'created_date', 'category']}),
	('Delete reminder ?',	{'fields': ['delete_rem'], 'classes': ['collapse']}),
	]
	list_display = ('remtitle_text', 'created_date', 'was_created_recently')	
	list_filter = ['created_date']
	search_fields = ['remname_text']

	
admin.site.register(Category, CategoryAdmin)
admin.site.register(Reminder, ReminderAdmin)
