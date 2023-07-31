# Generated by Django 4.2 on 2023-05-04 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estimate', '0003_remove_worktype_margin_w_remove_worktype_quantity_w'),
    ]

    operations = [
        migrations.AddField(
            model_name='worktype',
            name='margin_w',
            field=models.PositiveIntegerField(default=1, verbose_name='Наценка'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worktype',
            name='quantity_w',
            field=models.PositiveIntegerField(default=1, verbose_name='Количество'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='worktype',
            name='title_w',
            field=models.CharField(blank=True, max_length=255, verbose_name='Вид Работы'),
        ),
        migrations.AlterField(
            model_name='worktype',
            name='unit_w',
            field=models.CharField(blank=True, help_text='Введите короткое название единицы измерения (максимум 10 символов). Пример:кв.м', max_length=10, verbose_name='Единица измерения'),
        ),
    ]
