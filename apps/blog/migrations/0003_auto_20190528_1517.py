# Generated by Django 2.0.6 on 2019-05-28 18:17

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='container',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
