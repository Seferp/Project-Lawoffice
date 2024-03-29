# Generated by Django 4.2 on 2023-04-11 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('excerpt', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts')),
            ],
        ),
    ]
