# Generated by Django 4.0 on 2022-04-08 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthApp', '0006_doctors_emailid'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientImage',
            fields=[
                ('username', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('img', models.ImageField(upload_to='media')),
            ],
        ),
    ]
