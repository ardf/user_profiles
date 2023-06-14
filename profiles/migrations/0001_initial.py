# Generated by Django 4.2.2 on 2023-06-14 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('bio', models.TextField(blank=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='img/profile_pictures/')),
            ],
        ),
    ]
