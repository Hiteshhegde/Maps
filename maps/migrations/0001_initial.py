# Generated by Django 3.2.6 on 2021-08-14 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Distance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(default='Los Angeles', max_length=120)),
                ('destination', models.CharField(default='New York', max_length=120)),
                ('distance', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]
