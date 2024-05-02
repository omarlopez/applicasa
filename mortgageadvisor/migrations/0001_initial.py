# Generated by Django 4.2.6 on 2024-02-14 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MortgageAdvisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('fullName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('secondLastName', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('broker', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=50)),
            ],
        ),
    ]