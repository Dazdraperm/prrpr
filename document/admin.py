from django.contrib import admin

from .models import SiteUser, Passport, CourseGroup, DisabilityGroup

admin.site.register(Passport)
admin.site.register(CourseGroup)
admin.site.register(DisabilityGroup)


@admin.register(SiteUser)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user',)
    list_filter = ('user',)