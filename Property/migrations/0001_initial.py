# Generated by Django 2.1 on 2018-08-27 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='img')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0.0)),
                ('types_property', models.CharField(choices=[('H', 'House'), ('A', 'Apartment'), ('S', 'Studio'), ('O', 'others')], default='O', max_length=1)),
                ('province', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('postcode', models.IntegerField(default=0)),
                ('capacity', models.PositiveIntegerField(default=0)),
                ('num_bathrooms', models.PositiveIntegerField(default=0)),
                ('num_bedrooms', models.PositiveIntegerField(default=0)),
                ('num_double_bed', models.PositiveIntegerField(default=0)),
                ('num_single_bed', models.PositiveIntegerField(default=0)),
                ('num_sofa_bed', models.PositiveIntegerField(default=0)),
                ('area', models.FloatField(default=0.0)),
                ('kitchen', models.BooleanField(default=False)),
                ('in_unit_washer', models.BooleanField(default=False)),
                ('wifi', models.BooleanField(default=False)),
                ('elevator', models.BooleanField(default=False)),
                ('heating', models.BooleanField(default=False)),
                ('ac', models.BooleanField(default=False)),
                ('tv', models.BooleanField(default=False)),
                ('blower', models.BooleanField(default=False)),
                ('bathtub', models.BooleanField(default=False)),
                ('parking', models.BooleanField(default=False)),
                ('gyms', models.BooleanField(default=False)),
                ('swimming_pool', models.BooleanField(default=False)),
                ('party', models.BooleanField(default=False)),
                ('pet', models.BooleanField(default=False)),
                ('smoking', models.BooleanField(default=False)),
                ('couple', models.BooleanField(default=False)),
                ('longitude', models.FloatField(default=0.0)),
                ('latitude', models.FloatField(default=0.0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.BooleanField(default=False)),
                ('user_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='images',
            name='pid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Property.pid+', to='Property.Property', verbose_name='owner'),
        ),
    ]