# Generated by Django 3.0.3 on 2021-06-07 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(help_text='Required. Inform a valid email address.', max_length=254),
        ),
    ]