# Generated by Django 4.2.1 on 2023-05-23 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlankProblem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('language', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('blank_answer', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CodingProblem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('language', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('input_format', models.CharField(max_length=200)),
                ('output_format', models.CharField(max_length=200)),
                ('hint', models.CharField(max_length=400)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OptionProblem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('language', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_correct', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
