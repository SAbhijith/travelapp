# Generated by Django 3.2.15 on 2022-09-03 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelproject1app', '0003_delete_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
            ],
        ),
    ]
