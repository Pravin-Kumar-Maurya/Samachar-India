# Generated by Django 3.2.4 on 2022-09-09 08:53

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_mynews'),
    ]

    operations = [
        migrations.CreateModel(
            name='videonews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vlink', models.CharField(max_length=200)),
                ('vhead', models.CharField(max_length=500)),
                ('vcategory', models.CharField(max_length=500)),
                ('vcity', models.CharField(max_length=50)),
                ('vdate', models.DateField()),
                ('vdes', tinymce.models.HTMLField()),
            ],
        ),
    ]