# Generated by Django 2.2.5 on 2019-09-23 04:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190923_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
