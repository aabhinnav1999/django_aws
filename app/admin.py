from django.contrib import admin
from app.models import customer,product
# Register your models here.

class cust(admin.ModelAdmin):
    list_display=['id','cname','cmob']

class prod(admin.ModelAdmin):
    list_display=['pname','pcost','cus']

admin.site.register(customer,cust)
admin.site.register(product,prod)