from django.contrib import admin
from .models import EnModel

class EnAdmin(admin.ModelAdmin):
	list_display=('name','en_dt')
	list_filter=('en_dt',)
# Register your models here.
admin.site.register(EnModel,EnAdmin)