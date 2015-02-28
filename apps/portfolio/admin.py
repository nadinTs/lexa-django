from django.contrib import admin
from portfolio.models import Category, Project, Artifact


class ArtifactInline(admin.StackedInline):
    model = Artifact
    extra = 3


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ArtifactInline]
    list_filter = ['pub_date']
    search_fields = ['title', 'lead']


admin.site.register(Category)
admin.site.register(Project, ProjectAdmin)

