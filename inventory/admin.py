from django.contrib import admin
from .models import Customer, Electronics, Phone, Rents

# Register your models here.
#admin.site.register(Customer)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('custid', 'fname', 'lname', 'email', 'street', 'city', 'state', 'zip')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Electronics)
admin.site.register(Phone)
admin.site.register(Rents)
