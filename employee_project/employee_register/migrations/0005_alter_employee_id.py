# Generated by Django 4.0.3 on 2022-03-26 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0004_alter_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
