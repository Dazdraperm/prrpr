from django.contrib import admin

from .models import SiteUser, Passport

admin.site.register(Passport)
admin.site.register(SiteUser)

