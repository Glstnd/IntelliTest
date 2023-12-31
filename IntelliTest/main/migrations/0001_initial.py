# Generated by Django 4.2.7 on 2023-11-17 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuizCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('details', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='QuizQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('opt_1', models.CharField(max_length=200)),
                ('opt_2', models.CharField(max_length=200)),
                ('opt_3', models.CharField(max_length=200)),
                ('opt_4', models.CharField(max_length=200)),
                ('level', models.CharField(max_length=100)),
                ('time_limit', models.IntegerField()),
                ('right_opt', models.CharField(max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.quizcategory')),
            ],
            options={
                'verbose_name_plural': 'Questions',
            },
        ),
    ]
