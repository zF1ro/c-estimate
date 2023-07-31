from django import forms
from .models import *
from django.forms import ModelForm, TextInput, Textarea, CheckboxInput, \
    NumberInput, IntegerField, CharField, HiddenInput
from django.core.exceptions import ValidationError


# class AddProjectForm(forms.Form):
#     title_p = forms.CharField(max_length=255, label="Название проекта")
#     description_p = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label="Описание проекта",
#                                     required=False)
#     is_published_p = forms.BooleanField(label="Публикация", required=False)


class AddProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('title_p', 'description_p', 'is_published_p')

        widgets = {
            'title_p': TextInput(attrs={
                'placeholder': 'Название проекта',
            }),
            'description_p': Textarea(attrs={
                'placeholder': 'Описание проекта'
            }),
            'is_published_p': CheckboxInput(attrs={
                'placeholder': 'Публикация'
            }),
        }


class AddPrjSecForm(ModelForm):
    class Meta:
        model = ProjectSection
        fields = ('title_s',)

        widgets = {
            'title_s': Textarea(attrs={
                'placeholder': 'Название секции проекта',
                'cols': '35',
                'rows': '3',
                'maxlength': 100,
                'class': "colortext",
            }),
        }


class AddWorkType(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    quantity_w = IntegerField(label='Количество',
        widget=NumberInput(attrs={'placeholder': 'Количество', 'min': 1,
                                  'style': "width: calc(7ch + 20px)", 'class': "colortext"}))
    # 'style': "width: calc(10ch + 20px)" # 80ch это size=80 20px это отступы и скроллер цифр


    class Meta:
        model = WorkType
        fields = ('title_w', 'quantity_w', 'unit_w', 'margin_w',)

        widgets = {
            'title_w': Textarea(attrs={
                'placeholder': 'Вид работы',
                'cols': '30',
                'rows': '2',
                'maxlength': 100,
                'class': "colortext"
            }),
            'unit_w': TextInput(attrs={
                'placeholder': 'Ед.изм',
                'maxlength': '10',
                'size': '3',
                'class': "colortext"
            }),
            'margin_w': NumberInput(attrs={
                'min': '0',
                'placeholder': 'Наценка',
                'max': '200',
                'style': "width: calc(3ch + 20px)",
                'class': "colortext"
            }),
        }



class ResKind(forms.Form):
    PEOPLE = 'p'
    TECH = 't'
    MAT = 'm'
    OVERHEADS = 'o'
    TYPE = [
        (PEOPLE, 'Люди'),
        (TECH, 'Техника'),
        (MAT, 'Материалы'),
        (OVERHEADS, 'Накладные'),
    ]
    choice = forms.ChoiceField(choices=TYPE, label="Вид используемого ресурса")


class AddResP(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    quantity_r = forms.IntegerField(label="Количество людей",
                    widget=NumberInput(attrs={'placeholder': 'Количество', 'min': 1, 'max': 2000000000,
                                              'style': "width: calc(3ch + 20px)", 'class': "colortext"}))
    day_cost_r = forms.IntegerField(label="Стоимость за день",
                    widget=NumberInput(attrs={'placeholder': 'Стоимость за день', 'min': 1, 'max': 2000000000,
                                              'style': "width: calc(8ch + 20px)", 'class': "colortext"}))

    class Meta:
        model = Resource
        fields = ('quantity_r', 'day_cost_r')


class AddResT(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    quantity_r = forms.IntegerField(label="Количество единиц одинаковой техники",
                    widget=NumberInput(attrs={'placeholder': 'Количество', 'min': 1, 'max': 2000000000,
                                              'style': "width: calc(3ch + 20px)", 'class': "colortext"}))
    day_cost_r = forms.IntegerField(label="Стоимость за день",
                    widget=NumberInput(attrs={'placeholder': 'Стоимость за день', 'min': 1, 'max': 2000000000,
                                              'style': "width: calc(8ch + 20px)", 'class': "colortext"}))

    class Meta:
        model = Resource
        fields = ('quantity_r', 'day_cost_r')


class AddResM(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    unit_r = forms.CharField(max_length=10, label="Наименование единицы измерения",
                 widget=TextInput(attrs={'placeholder': 'Ед.изм.', 'size': 4, 'class': "colortext"}))
    quantity_r = forms.IntegerField(label="Количество",
                 widget=NumberInput(attrs={'placeholder': 'Количество', 'min': 1, 'max': 2000000000,
                                          'style': "width: calc(3ch + 20px)", 'class': "colortext"}))
    unit_cost_r = forms.IntegerField(label="Стоимость за единицу",
                 widget=NumberInput(attrs={'placeholder': 'цена ед.', 'min': 1, 'max': 2000000000,
                                           'style': "width: calc(8ch + 20px)", 'class': "colortext"}))

    class Meta:
        model = Resource
        fields = ('quantity_r', 'unit_r', 'unit_cost_r')


class AddResO(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    overhead_r = forms.CharField(max_length=255, label="Наименование накладной",
                 widget=Textarea(attrs={'placeholder': 'Наименование Накладной', 'class': "colortext",
                                        'cols': '30', 'rows': '2', 'maxlength': 100}))
    cost_r = forms.IntegerField(label="Сумма затрат",
                widget=NumberInput(attrs={'placeholder': 'Цена накладной', 'min': 1,  'max': 2000000000,
                                          'style': "width: calc(8ch + 20px)", 'class': "colortext"}))

    class Meta:
        model = Resource
        fields = ('overhead_r', 'cost_r')


class AskForm(forms.Form):
    ask = forms.BooleanField(label="Вы уверенны?")


    # sect = forms.ModelChoiceField(queryset=ProjectSection.objects.all(), label="Секция проекта")
    # prj_w = forms.ModelChoiceField(queryset=Project.objects.all(), label="Проект")
