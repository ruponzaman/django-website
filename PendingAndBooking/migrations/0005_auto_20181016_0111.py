# Generated by Django 2.0.5 on 2018-10-16 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PendingAndBooking', '0004_auto_20181002_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transandreview',
            name='comment_content',
            field=models.CharField(default='danjieniubi', max_length=500),
        ),
    ]