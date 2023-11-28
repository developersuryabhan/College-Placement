# Generated by Django 4.2.7 on 2023-11-28 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placement_app', '0002_alter_interviews_interview_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='email',
            field=models.EmailField(max_length=80, unique=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='gpa',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='students',
            name='roll_number',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]