# Generated by Django 3.2.7 on 2022-12-09 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DocFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('filepath', models.CharField(max_length=999, null=True)),
                ('filename', models.CharField(max_length=256, null=True)),
            ],
        ),
    ]
