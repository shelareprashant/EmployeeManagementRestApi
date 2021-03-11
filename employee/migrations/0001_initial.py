# Generated by Django 3.1.7 on 2021-03-11 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('doj', models.DateField()),
                ('email_id', models.EmailField(max_length=254)),
                ('mobile_no', models.CharField(max_length=15)),
                ('designation', models.CharField(max_length=20)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=9)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
    ]
