from django.contrib import admin
from .models import *

class AdminCustomerModel(admin.ModelAdmin):
    list_display=['customer_id','name','phone','email','address']
admin.site.register(CustomerModel,AdminCustomerModel)

class AdminCardTypesModel(admin.ModelAdmin):
    list_display=['card_type_id','name','limit','description',]
admin.site.register(CardTypesModel,AdminCardTypesModel)

class AdminRequestModel(admin.ModelAdmin):
    list_display=['id','card_type_id','customer_id','status','remark']
admin.site.register(RequestModel,AdminRequestModel)

class AdminLimitIncreaseRequestModel(admin.ModelAdmin):
    list_display=['id','card_type_id','final_limit','status','remark']
admin.site.register(LimitIncreaseRequestModel,AdminLimitIncreaseRequestModel)

class AdminCardDetailsModel(admin.ModelAdmin):
    list_display=['id','customer_id','card_type_id','card_number','card_limit','issued_date','expiration_date','is_blocked']
admin.site.register(CardDetailsModel,AdminCardDetailsModel)
