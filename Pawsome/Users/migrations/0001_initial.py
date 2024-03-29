# Generated by Django 4.0.4 on 2022-06-09 13:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Calendar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50)),
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('profile_image', models.ImageField(default='Logo-small.png', max_length=255, upload_to='logo_transparent.png')),
                ('role', models.CharField(choices=[('org', 'Organizations'), ('pros', 'Professional'), ('pet-owner', 'Pet Owner')], max_length=50)),
                ('events', models.ManyToManyField(to='Calendar.events')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Organizations',
            fields=[
                ('users_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('AFM', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('hours', models.TimeField()),
                ('telephone', models.CharField(max_length=12)),
            ],
            options={
                'abstract': False,
            },
            bases=('Users.users',),
        ),
        migrations.CreateModel(
            name='Professional',
            fields=[
                ('users_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('AFM', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('hours', models.TimeField(default='00:00')),
                ('telephone', models.CharField(max_length=12)),
                ('certificate', models.FileField(upload_to='')),
                ('CV', models.FileField(upload_to='')),
                ('speciality', models.CharField(choices=[('Vet', 'Vet'), ('pet-trainer', 'Pet Trainer'), ('pet-sitter', 'Pet sitter')], max_length=50)),
                ('license', models.FileField(upload_to='')),
                ('appointment', models.ManyToManyField(to='Calendar.appointment')),
            ],
            options={
                'abstract': False,
            },
            bases=('Users.users',),
        ),
        migrations.CreateModel(
            name='PetOwner',
            fields=[
                ('users_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('appointment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Calendar.appointment')),
            ],
            options={
                'abstract': False,
            },
            bases=('Users.users',),
        ),
    ]
