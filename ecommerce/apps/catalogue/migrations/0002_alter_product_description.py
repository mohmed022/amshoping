# Generated by Django 3.2 on 2021-09-14 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='description'),
        ),
    ]