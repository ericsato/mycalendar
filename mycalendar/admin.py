from django.contrib import admin
from mycalendar.models import Date, Type, Relationship

# Register your models here.
class DateAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}

class TypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class RelationshipAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('relationship',)}

admin.site.register(Date, DateAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Relationship, RelationshipAdmin)

