from django.contrib import admin
from .models import WnModel

class WnAdmin(admin.ModelAdmin):
	list_display=('name','wn_d','wn_t')
	list_filter=('wn_d','wn_t')
# Register your models here.

admin.site.register(WnModel,WnAdmin)