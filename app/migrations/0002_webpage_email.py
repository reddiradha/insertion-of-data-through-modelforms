# Generated by Django 4.1.4 on 2023-04-20 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='webpage',
            name='email',
            field=models.EmailField(default='cricket@gmail.com', max_length=254),
        ),
    ]