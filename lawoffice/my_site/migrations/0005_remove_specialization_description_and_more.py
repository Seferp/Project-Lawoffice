# Generated by Django 4.2 on 2023-04-14 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0004_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialization',
            name='description',
        ),
        migrations.RemoveField(
            model_name='specialization',
            name='excerpt',
        ),
        migrations.RemoveField(
            model_name='specialization',
            name='images',
        ),
        migrations.AddField(
            model_name='specialization',
            name='information',
            field=models.JSONField(default=1),
            preserve_default=False,
        ),
    ]
