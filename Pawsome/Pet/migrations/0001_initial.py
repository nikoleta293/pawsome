# Generated by Django 4.0.4 on 2022-05-31 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0001_initial'),
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
                ('img', models.ImageField(upload_to='D:\\Pawsome\\Pawsome\\Images')),
                ('pet_owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Users.petowner')),
            ],
        ),
    ]
