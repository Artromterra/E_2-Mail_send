# Generated by Django 3.0.3 on 2020-02-20 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('delay', models.SmallIntegerField()),
            ],
        ),
    ]
