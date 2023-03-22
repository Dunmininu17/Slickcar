# Generated by Django 4.1.2 on 2022-10-27 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=70)),
                ('message', models.TextField()),
                ('sent', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]