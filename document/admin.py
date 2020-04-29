from django.contrib import admin

from .models import Site, Passport, CourseGroup

admin.site.register(Passport)
admin.site.register(CourseGroup)


@admin.register(Site)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pFact',)
    list_filter = ('dateBirthday',)
