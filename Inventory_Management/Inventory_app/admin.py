from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
     list_display=['cat_name']
     search_fields=['cat_name']
admin.site.register(Category,CategoryAdmin)

class SettingsAdmin(admin.ModelAdmin):
    list_display=['store_name']
    search_fields=['store_name']
admin.site.register(Settings,SettingsAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=['cat_name','product_name','in_stock','min_stock']
    search_fields=['product_name']
admin.site.register(Product,ProductAdmin)

class LaboursAdmin(admin.ModelAdmin):
    list_display=['lab_name','phone_no','salary']
    search_fields=['lab_name']
admin.site.register(Labours,LaboursAdmin)

class SuppliersAdmin(admin.ModelAdmin):
    list_display=['supplier_name','phone_number','total_purchase','purchase_due']
    search_fields=['supplier_name']
admin.site.register(Suppliers,SuppliersAdmin)

class SalesreportAdmin(admin.ModelAdmin):
    list_display=['date','amount']
    search_fields=['date']
admin.site.register(Salesreport,SalesreportAdmin)
