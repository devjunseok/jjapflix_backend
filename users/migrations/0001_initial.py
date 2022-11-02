# Generated by Django 4.1.3 on 2022-11-02 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('nickname', models.CharField(blank=True, max_length=50)),
                ('profile_image', models.ImageField(blank=True, upload_to='profile_images/')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('movie', models.ManyToManyField(blank=True, related_name='movies', to='users.user')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
