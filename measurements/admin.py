from django.contrib import admin
from .models import Project, Measurement


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'created_at', 'updated_at']

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['pk', 'project', 'value', 'image']