# Generated by Django 4.1.3 on 2022-11-02 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='category',
            field=models.CharField(max_length=20, null=True),
        ),
    ]