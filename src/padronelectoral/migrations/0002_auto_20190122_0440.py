# Generated by Django 2.1.5 on 2019-01-22 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('padronelectoral', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='canton',
            name='stats_female',
            field=models.IntegerField(default=-1, null=True),
        ),
        migrations.AddField(
            model_name='canton',
            name='stats_male',
            field=models.IntegerField(default=-1, null=True),
        ),
        migrations.AddField(
            model_name='canton',
            name='stats_total',
            field=models.IntegerField(default=-1, null=True),
        ),
        migrations.AddField(
            model_name='province',
            name='stats_female',
            field=models.IntegerField(default=-1, null=True),
        ),
        migrations.AddField(
            model_name='province',
            name='stats_male',
            field=models.IntegerField(default=-1, null=True),
        ),
        migrations.AddField(
            model_name='province',
            name='stats_total',
            field=models.IntegerField(default=-1, null=True),
        ),
    ]
