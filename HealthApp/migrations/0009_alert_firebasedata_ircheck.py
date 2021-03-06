# Generated by Django 4.0 on 2022-04-13 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthApp', '0008_patients_age_patients_bloodtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='FirebaseData',
            fields=[
                ('username', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('Temp', models.FloatField()),
                ('IR', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='IRCheck',
            fields=[
                ('PositivePrev', models.BooleanField()),
                ('username', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('TimeStamp', models.FloatField()),
            ],
        ),
    ]
