# Generated by Django 4.0.3 on 2022-06-17 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0015_num_of_building'),
    ]

    operations = [
        migrations.AddField(
            model_name='num_of_building',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='num_of_building',
            name='information',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bookingapp.clinic'),
        ),
        migrations.AlterField(
            model_name='num_of_building',
            name='num',
            field=models.IntegerField(null=True),
        ),
    ]