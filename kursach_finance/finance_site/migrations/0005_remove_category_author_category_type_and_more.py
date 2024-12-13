# Generated by Django 5.1.1 on 2024-12-12 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance_site', '0004_alter_category_options_remove_category_slug_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='author',
        ),
        migrations.AddField(
            model_name='category',
            name='type',
            field=models.BooleanField(default=1, verbose_name='Тип операции'),
        ),
        migrations.AlterField(
            model_name='finance_site',
            name='operation_type',
            field=models.CharField(choices=[('Income', 'Доход'), ('Expenses', 'Расход'), ('None', 'Не выбрано')], default='None', max_length=10, verbose_name='Тип операции'),
        ),
    ]