# Generated by Django 5.0.6 on 2024-06-04 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bhuvi1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('photo', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
