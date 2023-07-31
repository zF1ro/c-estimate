# Представления для приложения estimate.

from .utils import FormMix
# from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.forms import formset_factory
from django.forms import modelformset_factory
from django.db.models import Q


def index(request):
    return render(request, 'estimate/index.html', {'title': 'Главная страница'})


def about(request):
    return render(request, 'estimate/about.html', {'title': 'О сайте'})


def all_projects(request):
    projects = Project.objects.all()
    context = {'title': 'Активные проекты', 'projects': projects}
    return render(request, 'estimate/all_projects.html', context=context)


def project(request, prj_id):
    """Отображение состава проекта"""
    prj = Project.objects.get(pk=prj_id)

    # all_sect = ProjectSection.objects.filter(prj=prj_id)
    all_sect = prj.projectsection_set.all()
    all_work = WorkType.objects.filter(prj_w=prj_id)
    # all_res = Resource.objects.filter(prj_r=prj_id)
    context = {'prj': prj, 'all_sect': all_sect, 'all_work': all_work}
    return render(request, 'estimate/project.html', context=context)


############################### Формы создания и добавления
def new_project(request):
    """Создание форм по всем модулям и предложения выбора ресурса,
     затем передача информации шаблону добавления вида ресурса"""
    # todo: (last) по завершению окончательного тестирования удалить вывод полной информации об ошибке на шаблон
    # TODO: Прописать валидаторы формы. Ввод только положительных чисел. \
    #  Длинное название единиц измерения. Проект с таким именем уже создан
    prj = None
    sect = None
    if request.method == 'POST':
        form_p = AddProjectForm(request.POST)
        form_s = AddPrjSecForm(request.POST)
        form_w = AddWorkType(request.POST)
        # Сохраняем проект
        if form_p.is_valid():
            try:
                prj = Project.objects.create(**form_p.cleaned_data)
            except:
                form_p.add_error(None, 'Ошибка создания проекта')

        # Сохраняем секцию
        if form_s.is_valid():
            try:
                form_s.cleaned_data['prj'] = prj
                sect = ProjectSection.objects.create(**form_s.cleaned_data)
            except:
                # Удаление созданного проекта при обнаружении ошибки создания секции проекта
                try:
                    prj.delete()
                except:
                    form_s.add_error(None, 'Ошибка удаления проекта')
                form_s.add_error(None, 'Ошибка создания секции проекта')

        # Сохраняем вид работы
        if form_w.is_valid():
            try:
                form_w.cleaned_data['prj_w'] = prj
                form_w.cleaned_data['sect'] = sect
                print(form_w.cleaned_data)
                WorkType.objects.create(**form_w.cleaned_data)
                return redirect('project', prj_id=prj.pk)
            except:
                try:
                    # Удаление созданной секции проекта и самого проекта при обнаружении ошибки создания вида работы.
                    prj.delete()
                    sect.delete()
                except:
                    form_w.add_error(None, f'Ошибка удаления секции проекта')
                form_w.add_error(None, f"Ошибка создания вида работы {form_w.add_error}\n{form_w.cleaned_data}")

    # Get зарос
    else:
        form_p = AddProjectForm()
        form_s = AddPrjSecForm()
        form_w = AddWorkType()
    context = {'title': 'Создание нового проекта', 'form_p': form_p,
               'form_s': form_s, 'form_w': form_w}
    return render(request, 'estimate/new_project.html', context=context)


def add_sect(request, prj_id):
    """Добавляем форму секции к проекту"""
    prj = Project.objects.get(pk=prj_id)
    all_sect = ProjectSection.objects.filter(prj=prj_id)
    all_work = WorkType.objects.filter(prj_w=prj_id)
    all_res = Resource.objects.filter(prj_r=prj_id)

    if request.method == 'POST':
        form_s = AddPrjSecForm(request.POST)
        if form_s.is_valid():
            try:
                form_s.cleaned_data['prj'] = prj
                print(f'добавлен ключ проекта {form_s.cleaned_data}')
                ProjectSection.objects.create(**form_s.cleaned_data)
                return redirect('project', prj_id=prj.pk)
            except:
                form_s.add_error(None, 'Ошибка создания секции проекта')

    else:
        form_s = AddPrjSecForm()
    context = {'prj': prj, 'all_sect': all_sect, 'all_work': all_work, 'all_res': all_res, 'form_s': form_s}
    return render(request, 'estimate/add_sect.html', context=context)


def add_work(request, prj_id, sect_id):
    """начинается проверка формы типа ресурса которую запросит шаблон с типом ресурса"""
    # todo: отфильтровать все секции относящиеся к проекту и передать их шаблону
    prj = Project.objects.get(pk=prj_id)
    sect = ProjectSection.objects.get(pk=sect_id)
    if request.method == 'POST':
        form_w = AddWorkType(request.POST)
        if form_w.is_valid():
            try:
                form_w.cleaned_data['prj_w'] = prj
                form_w.cleaned_data['sect'] = sect
                # print(f'добавлен ключ секции {form_w.cleaned_data}')
                WorkType.objects.create(**form_w.cleaned_data)
                return redirect('project_table', prj_id=prj.pk)
            except:
                form_w.add_error(None, "Ошибка создания вида работы")
    else:
        form_w = AddWorkType()
    context = {'prj': prj, 'form_w': form_w, 'sect': sect}
    return render(request, 'estimate/add_work.html', context=context)


def add_res_choice(request, prj_id, sect_id, work_id):
    prj = Project.objects.get(pk=prj_id)
    sect = ProjectSection.objects.get(pk=sect_id)
    work = WorkType.objects.get(pk=work_id)
    if request.method == 'POST':
        form_choice = ResKind(request.POST)
        if form_choice.is_valid():
            choice = form_choice.cleaned_data['choice']
            return redirect('add_res', prj_id=prj.pk, sect_id=sect.pk, work_id=work.pk, choice=choice)
    else:
        form_choice = ResKind()
    context = {'prj': prj, 'form_w': form_choice, 'sect': sect, 'work': work}
    return render(request, 'estimate/add_res_choice.html', context=context)


def add_res(request, prj_id, sect_id, work_id, choice):
    """уменьшил дублирование кода созданием класса аля миксин FormMix. """
    form_r = None
    prj = Project.objects.get(pk=prj_id)
    sect = ProjectSection.objects.get(pk=sect_id)
    work = WorkType.objects.get(pk=work_id)
    if request.method == 'POST':
        if choice == 'p':
            form_r = AddResP(request.POST)
            class_form = FormMix(form_r, prj_id, sect_id, work_id, choice)
            class_form.forms()
            return redirect('project_table', prj_id=prj_id)

        if choice == 't':
            form_r = AddResT(request.POST)
            class_form = FormMix(form_r, prj_id, sect_id, work_id, choice)
            class_form.forms()
            return redirect('project_table', prj_id=prj_id)

        if choice == 'm':
            form_r = AddResM(request.POST)
            class_form = FormMix(form_r, prj_id, sect_id, work_id, choice)
            class_form.forms()
            return redirect('project_table', prj_id=prj_id)

        if choice == 'o':
            form_r = AddResO(request.POST)
            class_form = FormMix(form_r, prj_id, sect_id, work_id, choice)
            class_form.forms()
            return redirect('project_table', prj_id=prj_id)

    else:
        if choice == 'p':
            form_r = AddResP()
        if choice == 't':
            form_r = AddResT()
        if choice == 'm':
            form_r = AddResM()
        if choice == 'o':
            form_r = AddResO()
    context = {'prj': prj, 'form_r': form_r, 'sect': sect, 'work': work, 'choice': choice}
    return render(request, 'estimate/add_res.html', context=context)



############################### Формы создания и добавления


############################### формы редактирования
def edit_project(request, prj_id):
    """редактирование Проекта"""
    prj = Project.objects.get(pk=prj_id)
    all_sect = prj.projectsection_set.all()
    all_work = prj.worktype_set.all()
    all_res = prj.resource_set.all()

    if request.method == 'POST':
        form_p = AddProjectForm(instance=prj, data=request.POST)
        if form_p.is_valid():
            form_p.save()
            return redirect('project', prj_id=prj_id)
    else:
        form_p = AddProjectForm(instance=prj)

    context = {'prj': prj, 'all_sect': all_sect, 'all_work': all_work, 'all_res': all_res, 'form_p': form_p}
    return render(request, 'estimate/edit_project.html', context=context)


def edit_section(request, prj_id, sect_id):
    prj = Project.objects.get(pk=prj_id)
    sect = ProjectSection.objects.get(pk=sect_id)
    all_sect = prj.projectsection_set.all()
    all_work = prj.worktype_set.all()
    all_res = prj.resource_set.all()

    if request.method == 'POST':
        form_s = AddPrjSecForm(instance=sect, data=request.POST)

        if form_s.is_valid():
            print(form_s)
            form_s.save()
            return redirect('project', prj_id=prj_id)
    else:
        form_s = AddPrjSecForm(instance=sect)
    context = {'prj': prj, 'all_sect': all_sect, 'all_work': all_work, 'all_res': all_res,
               'form_s': form_s, 'sect': sect}
    return render(request, 'estimate/edit_sect.html', context=context)



def edit_all(request, prj_id, sect_id):
    prj = Project.objects.get(pk=prj_id)
    sect = ProjectSection.objects.get(pk=sect_id)
    queryset_w = WorkType.objects.filter(sect_id=sect_id)
    forms_list = []
    valid = []

    if request.method == 'POST':
        print(request.POST)
        form_s = AddPrjSecForm(instance=sect, data=request.POST, prefix='sect')
        valid.append(form_s.is_valid())
        if form_s.is_valid():
            form_s.save()
        else:
            form_s.add_error(None, f"Ошибка ввода данных секции {sect.pk}")

        formset_w = []
        for work in queryset_w:
            form_w = AddWorkType(instance=work, data=request.POST, prefix=f'work{work.pk}')
            formset_w.append([form_w, work])
            valid.append(form_w.is_valid())
            if form_w.is_valid():
                form_w.save()

            else:
                form_w.add_error(None, f"Ошибка ввода данных вида работы {work.pk} "
                                   f"\n{form_w.add_error}\n{form_w.cleaned_data}")

            queryset_r = Resource.objects.filter(work_id=work.pk)

            formset_r = []
            for res in queryset_r:
                if res.title_r == 'p':
                    form_r = AddResP(instance=res, data=request.POST, prefix=f'res_p{res.pk}')
                    formset_r.append([form_r, res])
                    valid.append(form_r.is_valid())
                    print(f'res_p{res.pk}: {form_r.is_valid()} \n {form_r.errors}')
                    if form_r.is_valid():
                        form_r.save()
                    else:
                        form_r.add_error(None, f"Ошибка ввода данных ресурса {res.pk} "
                                               f"\n{form_r.add_error}\n{form_r.cleaned_data}")

                if res.title_r == 't':
                    form_r = AddResT(instance=res, data=request.POST, prefix=f'res_t{res.pk}')
                    formset_r.append([form_r, res])
                    valid.append(form_r.is_valid())
                    print(f'res_t{res.pk}: {form_r.is_valid()}')
                    if form_r.is_valid():
                        form_r.save()
                    else:
                        form_r.add_error(None, f"Ошибка ввода данных ресурса {res.pk} "
                                               f"\n{form_r.add_error}\n{form_r.cleaned_data}")

                if res.title_r == 'm':
                    form_r = AddResM(instance=res, data=request.POST, prefix=f'res_m{res.pk}')
                    formset_r.append([form_r, res])
                    valid.append(form_r.is_valid())
                    print(f'res_m{res.pk}: {form_r.is_valid()}')
                    if form_r.is_valid():
                        form_r.save()
                    else:
                        form_r.add_error(None, f"Ошибка ввода данных ресурса {res.pk} "
                                               f"\n{form_r.add_error}\n{form_r.cleaned_data}")

                if res.title_r == 'o':
                    form_r = AddResO(instance=res, data=request.POST, prefix=f'res_o{res.pk}')
                    formset_r.append([form_r, res])
                    valid.append(form_r.is_valid())
                    print(f'res_o{res.pk}: {form_r.is_valid()}')
                    if form_r.is_valid():
                        form_r.save()
                    else:
                        form_r.add_error(None, f"Ошибка ввода данных ресурса {res.pk} "
                                               f"\n{form_r.add_error}\n{form_r.cleaned_data}")
            forms_list.append([form_w, work, formset_r])

        if all(valid):
            return redirect('project_table', prj_id=prj_id)

    else:
        form_s = AddPrjSecForm(instance=sect, prefix='sect')
        for work in queryset_w:
            form_w = AddWorkType(instance=work, prefix=f'work{work.pk}')

            queryset_r = Resource.objects.filter(work_id=work.pk)
            formset_r = []
            for res in queryset_r:
                if res.title_r == 'p':
                    form_r = AddResP(instance=res, prefix=f'res_p{res.pk}')
                    formset_r.append([form_r, res])

                if res.title_r == 't':
                    form_r = AddResT(instance=res, prefix=f'res_t{res.pk}')
                    formset_r.append([form_r, res])

                if res.title_r == 'm':
                    form_r = AddResM(instance=res, prefix=f'res_m{res.pk}')
                    formset_r.append([form_r, res])

                if res.title_r == 'o':
                    form_r = AddResO(instance=res, prefix=f'res_o{res.pk}')
                    formset_r.append([form_r, res])

            forms_list.append([form_w, work, formset_r])


    context = {'prj': prj, 'title': 'Редактирование проекта',
               'sect': sect, 'forms_list': forms_list, 'form_s': form_s}
    return render(request, 'estimate/edit_all.html', context=context)


def ask_for_delete(request, obj_type, obj_id, prj_id, sect_id):
    obj = None
    sect = ProjectSection.objects.get(pk=sect_id)
    prj = Project.objects.get(pk=prj_id)

    if request.method == 'POST':
        if obj_type == 'prj':
            obj = Project.objects.get(pk=obj_id)
            obj.delete()
        if obj_type == 'sect':
            obj = ProjectSection.objects.get(pk=obj_id)
            obj.delete()
        if obj_type == 'work':
            obj = WorkType.objects.get(pk=obj_id)
            obj.delete()
        if obj_type == 'res':
            obj = Resource.objects.get(pk=obj_id)
            obj.delete()

        return redirect('edit_all', prj_id, sect_id)
    else:
        if obj_type == 'prj':
            obj = Project.objects.get(pk=obj_id)
        if obj_type == 'sect':
            obj = ProjectSection.objects.get(pk=obj_id)
        if obj_type == 'work':
            obj = WorkType.objects.get(pk=obj_id)
        if obj_type == 'res':
            obj = Resource.objects.get(pk=obj_id)


    context = {'obj': obj, 'obj_type': obj_type, 'sect': sect, 'prj': prj}
    return render(request, 'estimate/ask_for_delete.html', context=context)




############################### формы редактирования


############################### отображение таблиц



def project_table(request, prj_id):
    """Отображение состава проекта"""
    prj = Project.objects.get(pk=prj_id)
    all_sect = prj.projectsection_set.all()
    all_work = prj.worktype_set.all()

    profit = 0
    total_cost = 0
    total_with_margin = 0
    if prj.total_with_margin():
        total_with_margin += prj.total_with_margin()

    if prj.total_cost():
        total_cost += prj.total_cost()

    if prj.total_with_margin() and prj.total_cost():
        profit = total_with_margin - total_cost

    profit_fo = "{:,.2f}".format(profit)
    total_cost_fo = "{:,.2f}".format(total_cost)
    total_with_margin_fo = "{:,.2f}".format(total_with_margin)

    context = {'prj': prj, 'all_sect': all_sect, 'all_work': all_work, 'total_with_margin_fo': total_with_margin_fo,
               'total_cost_fo': total_cost_fo, 'profit_fo': profit_fo, }
    return render(request, 'estimate/project_table.html', context=context)



def page(request):
    n_res = range(0, 4)
    n_res_len = int(len(n_res) + 2)
    n_works = range(0, 4)
    n_sect = range(0, 3)
    context = {'n_res': n_res, 'n_works': n_works, 'n_sect': n_sect, 'n_res_len': n_res_len}
    return render(request, 'estimate/page.html', context=context)
############################### отображение таблиц


def login(request):
    return render(request, 'estimate/base(in_process).html', {'title': 'Вход в личный кабинет'})


##!!! from django.db.models import Q
# sect = ProjectSection.objects.get(Q(title_s=form_s.cleaned_data['title_s']) & Q(prj=prj))

####################### Тест сетов






#######################


















