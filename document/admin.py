from django.contrib import admin

from .models import SiteUser, Passport, CourseGroup

admin.site.register(Passport)
admin.site.register(CourseGroup)


@admin.register(SiteUser)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pFact',)
    list_filter = ('dateBirthday',)
