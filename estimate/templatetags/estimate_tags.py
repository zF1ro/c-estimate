from django import template
from estimate.models import *
from django.forms import modelformset_factory
from django import forms
from estimate.forms import *

register = template.Library()


@register.simple_tag()
def return_menu():
    menu = [
        {'title': "Главная страница", 'url_name': 'index'},
        {'title': "О сайте", 'url_name': 'about'},
        {'title': "Проекты", 'url_name': 'all_projects'},
        {'title': 'Таблица(Временная)', 'url_name': 'page'},
        {'title': "Войти", 'url_name': 'login'}
    ]
    return menu


@register.inclusion_tag('estimate/list_res.html')
def list_res(work):
    all_res = work.resource_set.all()
    return {'all_res': all_res}


@register.inclusion_tag('estimate/list_works.html')
def list_works(prj, sect):
    all_work = sect.worktype_set.all()
    return {'all_work': all_work, 'prj': prj, 'sect': sect}


@register.simple_tag()
def set_len_sec(s, for_form=False):
    """Подсчет объектов для вычисления высоты (rowspan) разделительного столбца с названием секции."""
    work_count = s.worktype_set.count()
    tr = 2  # коэффициент. если таблица не содержит форм, у каждого вида работы будет дополнительно 2 строки,
    # строка с опцией добавления ресурса и разделяющая цветная строка.
    res_count = 0
    works = s.worktype_set.all()
    if works:
        for w in works:
            if w.resource_set.count():
                res_count += (w.resource_set.count() + 1)
            else:
                res_count += 1
    if for_form:
        tr = 3
    rowspan = res_count + (work_count * tr) + 1
    return rowspan


@register.inclusion_tag('estimate/tag_show_res.html')
def show_res(r):
    total_cost_r_fo = "{:,.2f}".format(r.total_cost())

    day_cost_r_fo = None
    if r.day_cost_r:
        day_cost_r_fo = "{:,.2f}".format(r.day_cost_r)

    cost_r_fo = None
    if r.cost_r:
        cost_r_fo = "{:,.2f}".format(r.cost_r)

    unit_cost_r_fo = None
    if r.unit_cost_r:
        unit_cost_r_fo = "{:,.2f}".format(r.unit_cost_r)

    unit_with_margin_r_fo = "{:,.2f}".format(r.unit_with_margin())
    total_with_margin_r_fo = "{:,.2f}".format(r.total_with_margin())

    return {'r': r, 'total_cost_r_fo': total_cost_r_fo, 'day_cost_r_fo': day_cost_r_fo,
            'cost_r_fo': cost_r_fo, 'total_with_margin_r_fo': total_with_margin_r_fo,
            'unit_with_margin_r_fo': unit_with_margin_r_fo, 'unit_cost_r_fo': unit_cost_r_fo}

#################### для таблицы
@register.simple_tag()
def total_cost_w(w):
    total_cost_w = round((w.total_cost()), 2)

    return "{:,.2f}".format(total_cost_w)


@register.simple_tag()
def unit_with_margin_w(w):
    unit_with_margin_w = w.total_with_margin() / w.quantity_w

    return "{:,.2f}".format(unit_with_margin_w)


@register.simple_tag()
def total_with_margin_w(w):
    total_coast_w = w.total_with_margin()

    return "{:,.2f}".format(total_coast_w)


@register.simple_tag()
def unit_cost_w(w):
    unit_cost_w = round((w.total_cost() / w.quantity_w), 2)

    return "{:,.2f}".format(unit_cost_w)


@register.simple_tag()
def total_cost_s(s):
    total_cost_s = s.total_cost()

    return "{:,.2f}".format(total_cost_s)


@register.simple_tag()
def total_with_margin_s(s):
    total_with_margin_s = s.total_with_margin()

    return "{:,.2f}".format(total_with_margin_s)


@register.inclusion_tag('estimate/tag_show_no_works.html')
def show_no_works(s):
    return {'s': s}


#################### для таблицы
#################### формы@


# @register.inclusion_tag('estimate/tag_delete_res.html')
# def delete_res(res, prj_id, sect_id):
#     return {'prj_id': prj_id, 'sect_id': sect_id}




@register.simple_tag()
def get_initial(form, field):
    return form.get_initial_for_field(form.fields[field], field)





#################### формы


































