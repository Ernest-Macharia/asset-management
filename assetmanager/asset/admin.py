from django.contrib import admin
from . models import Asset,Appreciate,Depreciate
from . forms import AssetForm,AppreciationForm,DepreciationForm
# Register your models here.

class AssetAdmin(admin.ModelAdmin):
	list_display = ['name','serial_number','acquisition_date','timestamp']
	form = AssetForm
	list_filter = ['name','serial_number']
	search_fields = ['name','serial_number']
class AppreciationAdmin(admin.ModelAdmin):
	list_display = ['name','amount','appreciation_rate','months']
	form = AssetForm
	list_filter = ['name','appreciation_rate']
	search_fields = ['name','appreciation_rate']
class DepreciationAdmin(admin.ModelAdmin):
	list_display = ['name','amount','depreciation_rate','months']
	form = AssetForm
	list_filter = ['name','depreciation_rate']
	search_fields = ['name','depreciation_rate']

admin.site.register(Asset, AssetAdmin)
admin.site.register(Appreciate, AppreciationAdmin)
admin.site.register(Depreciate, DepreciationAdmin)