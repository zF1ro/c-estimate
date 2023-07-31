# from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.db.models import Q


class FormMix:
    """Миксин для добавления ресурса. Убирает дублирование кода."""
    def __init__(self, form_r, prj_id, sect_id, work_id, choice):
        self.form_r = form_r
        self.prj_id = prj_id
        self.sect_id = sect_id
        self.work_id = work_id
        self.choice = choice


    def forms(self):
        prj = Project.objects.get(pk=self.prj_id)
        work = WorkType.objects.get(pk=self.work_id)
        if self.form_r.is_valid():
            try:
                dict_ad = {'prj_r': prj, 'work': work, 'title_r': self.choice}
                Resource.objects.create(**(self.form_r.cleaned_data | dict_ad))

            except:
                self.form_r.add_error(None, "Ошибка создания ресурса")










