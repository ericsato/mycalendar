from django.contrib import admin
from mycal.models import Date, Type

# Register your models here.
class DateAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}

class TypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Date, DateAdmin)
admin.site.register(Type, TypeAdmin)
