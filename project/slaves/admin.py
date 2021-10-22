from django.contrib import admin

from . import models


@admin.register(models.Resume)
class ResumeAdmin(admin.ModelAdmin):
    class PlaceInline(admin.TabularInline):
        model = models.Place
        fields = ('title', 'position', 'started_in', 'finished_in')
        extra = 0

    list_display = ('title', 'owner', 'money', 'registered_in')
    inlines = (PlaceInline, )


@admin.register(models.Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'resume', 'position', 'started_in',
                    'finished_in', 'registered_in')
