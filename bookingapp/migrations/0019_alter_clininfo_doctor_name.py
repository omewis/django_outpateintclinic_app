# Generated by Django 4.0.3 on 2022-06-17 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0018_alter_clininfo_doctor_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clininfo',
            name='doctor_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
