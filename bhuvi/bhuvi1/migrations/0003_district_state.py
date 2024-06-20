# Generated by Django 5.0.6 on 2024-06-13 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bhuvi1', '0002_tech'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=50, verbose_name='dist')),
            ],
            options={
                'db_table': 'tbl_dist',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=50, verbose_name='state')),
                ('district', models.CharField(max_length=50, verbose_name='dist')),
            ],
            options={
                'db_table': 'tbl_state',
            },
        ),
    ]
