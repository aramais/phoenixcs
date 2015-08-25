from django.contrib import admin

from .models import preliminaryRegistration

class preliminaryRegistrationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in preliminaryRegistration._meta.fields if field.name != "id"]

admin.site.register(preliminaryRegistration, preliminaryRegistrationAdmin)
