from django.contrib import admin

from .models import Project

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    # Placeholder for customisation
    pass


admin.site.register(Project, ProjectAdmin)
