# Generated by Django 2.1.5 on 2019-01-18 04:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Canton',
            fields=[
                ('code', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('codelec', models.PositiveIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(999999)])),
                ('name', models.CharField(max_length=34)),
                ('stats_female', models.IntegerField(default=-1, null=True)),
                ('stats_male', models.IntegerField(default=-1, null=True)),
                ('stats_total', models.IntegerField(default=-1, null=True)),
                ('canton', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='padronelectoral.Canton')),
            ],
        ),
        migrations.CreateModel(
            name='Elector',
            fields=[
                ('idCard', models.PositiveIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(999999999)])),
                ('gender', models.SmallIntegerField(choices=[(1, 'Male'), (2, 'Female')])),
                ('cad_date', models.DateField()),
                ('board', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999999)])),
                ('fullName', models.CharField(max_length=100)),
                ('codelec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='padronelectoral.District')),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.SmallIntegerField()),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='canton',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='padronelectoral.Province'),
        ),
    ]
