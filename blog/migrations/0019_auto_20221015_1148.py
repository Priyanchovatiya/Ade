# Generated by Django 3.2.8 on 2022-10-15 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20221014_2351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='fb',
        ),
        migrations.RemoveField(
            model_name='team',
            name='insta',
        ),
        migrations.RemoveField(
            model_name='team',
            name='twitter',
        ),
        migrations.RemoveField(
            model_name='team',
            name='youtube',
        ),
        migrations.AddField(
            model_name='team',
            name='role',
            field=models.CharField(max_length=1256, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='position',
            field=models.CharField(max_length=1156),
        ),
    ]
