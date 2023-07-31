from django.contrib import admin
from .models import *


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_p', 'time_create_p', 'is_published_p')
    list_display_links = ('id', 'title_p')
    search_fields = ('title_p', )
    list_editable = ('is_published_p',)
    list_filter = ('time_create_p', )


class ProjectSectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_s', 'prj', 'time_create_s', 'is_published_s')
    list_editable = ('is_published_s',)
    list_display_links = ('id', 'title_s')
    search_fields = ('title_s', )
    list_filter = ('time_create_s', 'prj')


class WorkTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_w', 'prj_w', 'sect', 'time_create_w')
    list_display_links = ('id', 'title_w', 'sect')
    search_fields = ('title_w', )
    list_filter = ('time_create_w', 'prj_w', 'sect')


class ResourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'prj_r', 'work', 'title_r', 'time_create_r')
    list_display_links = ('id', 'title_r')
    search_fields = ('title_r', )
    list_filter = ('time_create_r', 'prj_r', 'work')


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectSection, ProjectSectionAdmin)
admin.site.register(WorkType, WorkTypeAdmin)
admin.site.register(Resource, ResourceAdmin)
