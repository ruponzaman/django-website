# Generated by Django 2.0.5 on 2018-09-10 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserAndAdmin', '0002_auto_20180910_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='language',
            field=models.CharField(default='English', max_length=10),
        ),
    ]