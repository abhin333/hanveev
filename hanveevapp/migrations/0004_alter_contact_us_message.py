# Generated by Django 4.0.1 on 2022-03-10 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hanveevapp', '0003_contact_us'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_us',
            name='message',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
