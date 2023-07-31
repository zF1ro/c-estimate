from django.urls import path
from .views import *
from .templatetags.estimate_tags import *


urlpatterns = [
    path('', index, name='index'),
    path('all_projects/', all_projects, name='all_projects'),
    path('about/', about, name='about'),
    path('login/', login, name='login'),
    path('project/<int:prj_id>/', project, name='project'),
    path('new_project/', new_project, name='new_project'),
    path('add_sect/<int:prj_id>', add_sect, name='add_sect'),
    path('add_work/<int:prj_id>/<int:sect_id>', add_work, name='add_work'),
    path('add_res_choice/<int:prj_id>/<int:sect_id>/<int:work_id>', add_res_choice, name='add_res_choice'),
    path('add_res/<int:prj_id>/<int:sect_id>/<int:work_id>/<str:choice>', add_res, name='add_res'),
    path('edit_project/<int:prj_id>', edit_project, name='edit_project'),
    path('edit_section/<int:prj_id>/<int:sect_id>', edit_section, name='edit_section'),
    path('page/', page, name='page'),
    path('project_table/<int:prj_id>', project_table, name='project_table'),
    path('edit_all/<int:prj_id>/<int:sect_id>', edit_all, name='edit_all'),
    path('ask_for_delete/<slug:obj_type>/<int:obj_id>//<int:prj_id>/<int:sect_id>', ask_for_delete, name='ask_for_delete'),
    #
]













