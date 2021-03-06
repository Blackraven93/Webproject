# Generated by Django 3.0.8 on 2020-07-15 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorName', models.CharField(max_length=50, verbose_name='저자이름')),
                ('authorExp', models.TextField(blank=True, verbose_name='저자설명')),
                ('authorEmail', models.EmailField(blank=True, max_length=30, verbose_name='저자이메일')),
            ],
        ),
    ]
