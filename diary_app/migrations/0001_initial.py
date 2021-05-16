# Generated by Django 3.2.3 on 2021-05-16 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_title', models.CharField(max_length=200)),
                ('entry_date', models.DateTimeField(verbose_name='date published')),
                ('entry_body', models.TextField()),
            ],
        ),
    ]
