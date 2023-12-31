# Generated by Django 4.2.4 on 2023-08-04 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('password', models.TextField(max_length=30)),
                ('phone', models.CharField(max_length=10)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_user', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superadmin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
