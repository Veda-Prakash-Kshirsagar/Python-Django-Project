from django.contrib import admin

# Register your models here.

from .models import Cofee

class CofeeAdmin(admin.ModelAdmin):
    list_display = ('name','price','quantity')

admin.site.register(Cofee,CofeeAdmin)
