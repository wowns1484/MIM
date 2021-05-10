# Generated by Django 3.0.8 on 2020-08-19 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField()),
                ('title', models.TextField()),
                ('cast', models.TextField()),
                ('characters', models.TextField()),
                ('summary', models.TextField()),
                ('famous_line', models.TextField()),
            ],
        ),
    ]