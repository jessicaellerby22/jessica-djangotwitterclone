# Generated by Django 4.1.7 on 2023-03-07 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.CharField(db_index=True, max_length=140, null=True, verbose_name='Body'),
        ),
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(db_index=True, default='Anonymous', max_length=14, null=True, verbose_name='Name'),
        ),
    ]
