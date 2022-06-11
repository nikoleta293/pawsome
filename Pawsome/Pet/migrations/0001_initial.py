# Generated by Django 4.0.4 on 2022-06-09 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_name', models.CharField(max_length=25)),
                ('age', models.CharField(max_length=4)),
                ('gender', models.CharField(max_length=6)),
                ('kind', models.CharField(max_length=100)),
                ('health_history', models.TextField()),
                ('img', models.ImageField(blank=True, default='../Images/logo.png', null=True, upload_to='Images/')),
            ],
        ),
    ]
