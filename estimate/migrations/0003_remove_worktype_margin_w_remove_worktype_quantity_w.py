# Generated by Django 4.2 on 2023-05-04 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estimate', '0002_alter_project_description_p_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worktype',
            name='margin_w',
        ),
        migrations.RemoveField(
            model_name='worktype',
            name='quantity_w',
        ),
    ]