# Generated by Django 4.2 on 2023-04-11 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0002_specialization'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialization',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
