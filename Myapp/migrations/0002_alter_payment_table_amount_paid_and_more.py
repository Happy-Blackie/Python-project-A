# Generated by Django 4.1.1 on 2022-09-10 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_table',
            name='Amount_Paid',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='payment_table',
            name='Phone_Number',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
