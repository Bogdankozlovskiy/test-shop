# Generated by Django 4.0.2 on 2022-02-03 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True, verbose_name='phone number'),
        ),
    ]
