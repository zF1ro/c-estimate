from django.db import models
from django.urls import reverse


class Project(models.Model):
    title_p = models.CharField(max_length=255, unique=True,
                               verbose_name="Название Проекта")  # атрибут title будет определять одноименное поле как текстовую строку с максимальным числом символов 255.
    description_p = models.TextField(verbose_name="Текст статьи", blank=True,
                                     null=True)  # поле задано как текстовое с параметром blank=True. Данный параметр означает, что это поле может быть пустым, то есть, не содержать текста.
    time_create_p = models.DateTimeField(auto_now_add=True,
                                         verbose_name="Время создания")  # auto_now_add – позволяет фиксировать текущее время только в момент первого добавления записи в таблицу БД;
    time_update_p = models.DateTimeField(auto_now=True,
                                         verbose_name="Время изменения")  # auto_now – фиксирует текущее время всякий раз при изменении или добавлении записи в таблицу БД.
    is_published_p = models.BooleanField(default=False, verbose_name="Публикация", blank=True,
                                         null=True)  # атрибут is_published определен через класс BooleanField с параметром default=True. Это означает, что по умолчанию значение поля в БД будет установлено в значение True и статья будет считаться опубликованной.

    def __str__(self):
        return self.title_p

    def get_absolute_url(self):
        return reverse('project', kwargs={'prj_id': self.pk})

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = '1.Проекты'
        ordering = ['-time_create_p', 'title_p']

    def total_cost(self):
        all_sect = self.projectsection_set.all()
        total_cost = 0
        for s in all_sect:
            total_cost += s.total_cost()
        return total_cost

    def total_with_margin(self):
        all_sect = self.projectsection_set.all()
        total_with_margin = 0
        for s in all_sect:
            total_with_margin += s.total_with_margin()
        return total_with_margin


class ProjectSection(models.Model):
    """Раздел Проекта."""
    title_s = models.CharField(max_length=255, verbose_name="Раздел Проекта", unique=False)
    time_create_s = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update_s = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published_s = models.BooleanField(default=False, verbose_name="Публикация", blank=True, null=True)
    prj = models.ForeignKey('Project', on_delete=models.CASCADE, null=False, verbose_name="Проект")

    def __str__(self):
        return self.title_s

    class Meta:
        verbose_name = 'Раздел проекта'
        verbose_name_plural = '2.Разделы проекта'
        ordering = ['-title_s']

    def total_cost(self):
        all_work = self.worktype_set.all()
        total_cost = 0
        for work in all_work:
            total_cost += work.total_cost()
        return total_cost

    def total_with_margin(self):
        all_work = self.worktype_set.all()
        total_with_margin_s = 0
        for work in all_work:
            total_with_margin_s += work.total_with_margin()
        return total_with_margin_s


class WorkType(models.Model):
    """Вид работы."""
    title_w = models.CharField(max_length=255, verbose_name="Название вида работы", unique=False)
    time_create_w = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update_w = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    quantity_w = models.PositiveIntegerField(verbose_name="Количество")
    unit_w = models.CharField(max_length=10, unique=False, verbose_name="Ед.изм.")
    margin_w = models.PositiveIntegerField(verbose_name="Наценка")
    sect = models.ForeignKey('ProjectSection', on_delete=models.CASCADE, null=False, verbose_name="Секция проекта")
    prj_w = models.ForeignKey('Project', on_delete=models.CASCADE, null=False, verbose_name="Проект")

    def __str__(self):
        return self.title_w

    class Meta:
        verbose_name = 'Вид работы'
        verbose_name_plural = '3.Вид работ'
        ordering = ['-time_create_w']

    def total_cost(self):
        all_res = self.resource_set.all()
        total_cost = 0
        for res in all_res:
            total_cost += res.total_cost()
        return total_cost

    def total_with_margin(self):
        all_res = self.resource_set.all()
        total_with_margin = 0
        for res in all_res:
            res_cost = res.total_cost()
            total_with_margin += res_cost + (res_cost * self.margin_w / 100)
        return total_with_margin




# todo: добавить еще титул в котором будет хранится более подробная информация о ресурсе. добавить временные параметры.



class Resource(models.Model):
    """Используемый ресурсы или дополнительные траты из доступного перечня: Люди, Техника, Материалы или Накладные."""
    PEOPLE = 'p'
    TECH = 't'
    MAT = 'm'
    OVERHEADS = 'o'
    TYPE = [
        (PEOPLE, 'Люди'),
        (TECH, 'Техника'),
        (MAT, 'Материалы или Оборудование'),
        (OVERHEADS, 'Накладные расходы')
    ]
    # unit_info =
    title_r = models.CharField(max_length=30, verbose_name="Ресурс", choices=TYPE, null=True, unique=False)
    time_create_r = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update_r = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    quantity_r = models.PositiveIntegerField(verbose_name="Количество", blank=True, null=True)
    day_cost_r = models.PositiveIntegerField(verbose_name="Стоимость за день", blank=True, null=True)
    #todo #изменить на дробное
    unit_cost_r = models.PositiveIntegerField(verbose_name="Стоимость за единицу", blank=True, null=True)
    unit_r = models.CharField(max_length=10, verbose_name="Единица измерения", blank=True, null=True)
    cost_r = models.PositiveIntegerField(verbose_name="Сумма затрат", blank=True, null=True)
    overhead_r = models.CharField(max_length=255, verbose_name="Наименование накладной", blank=True, null=True)
    # days_q = models.PositiveIntegerField

    work = models.ForeignKey('WorkType', on_delete=models.CASCADE, null=False, verbose_name="Вид работы")
    prj_r = models.ForeignKey('Project', on_delete=models.CASCADE, null=False, verbose_name="Проект")

    def __str__(self):
        return self.title_r

    class Meta:
        verbose_name = 'Тип ресурса'
        verbose_name_plural = '4.Типы Ресурсов'
        ordering = ['-time_create_r']

    def unit_with_margin(self):
        unit_with_margin = 0
        if self.title_r == 'p' or self.title_r == 't':
            unit_with_margin = self.day_cost_r + (self.day_cost_r * self.work.margin_w / 100)

        if self.title_r == 'm':
            unit_with_margin = self.unit_cost_r + (self.unit_cost_r * self.work.margin_w / 100)

        if self.title_r == 'o':
            unit_with_margin = self.cost_r + (self.cost_r * self.work.margin_w / 100)

        return unit_with_margin

    def total_cost(self):
        # временно количество дней будет 30
        days = 30
        total_cost = 0

        if self.title_r == 'p' or self.title_r == 't':
            total_cost = days * self.quantity_r * self.day_cost_r

        if self.title_r == 'm':
            total_cost = self.quantity_r * self.unit_cost_r

        if self.title_r == 'o':
            total_cost = self.cost_r

        return total_cost

    def total_with_margin(self):
        total_coast = self.total_cost()
        margin = self.work.margin_w
        total_with_margin = total_coast + (total_coast * margin / 100)
        return total_with_margin




##!! from estimate.models import *


# w.objects.create('title_w': '333', 'quantity_w': 333, 'unit_w': '333', 'margin_w': 333, 'prj': <Project: 1>, 'sect': <ProjectSection: 1>)
