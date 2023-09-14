# Generated by Django 3.2.4 on 2022-09-02 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='igallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gname', models.CharField(max_length=400)),
                ('gpic', models.ImageField(default='', upload_to='static/gallery/')),
            ],
        ),
        migrations.CreateModel(
            name='slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shead', models.CharField(max_length=300)),
                ('ssubject', models.CharField(max_length=300)),
                ('sdes', models.TextField()),
                ('spic', models.ImageField(default='', upload_to='static/slider/')),
            ],
        ),
    ]
