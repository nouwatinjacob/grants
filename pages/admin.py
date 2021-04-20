from django.contrib import admin

from .models import Application

# Register your models here.

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'prefix', 'referral', 'first_name', 'last_name',
                  'middle_name', 'dob', 'mother_name', 'relationship', 'gender',
                  'occupation', 'ssn', 'address', 'state', 'nationality',
                  'phone', 'fax', 'income', 'email', 'bank', 'front_id', 'back_id', 'description')
    search_fields = ['first_name', 'last_name', 'ssn']
    
    
    
admin.site.register(Application, ApplicationAdmin)