from django.contrib import admin
from Property.models import State,City,Category,Property,ContactUs
from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Register your models here.

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('id','name')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id','name','state_id','state')
    list_filter = ('state',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name',)

# import property fro import_export
class PropertyResource(resources.ModelResource):

    class Meta:
        model = Property
       
class PropertyAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','name','category','city','state',)

admin.site.register(Property, PropertyAdmin)


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('id','username','email')



