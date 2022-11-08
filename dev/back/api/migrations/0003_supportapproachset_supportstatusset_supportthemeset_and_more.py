# Generated by Django 4.1.3 on 2022-11-08 05:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_office_options_alter_officetypeset_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupportApproachSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elem', models.CharField(max_length=32, verbose_name='支援・受講方法')),
            ],
            options={
                'verbose_name': '支援・受講方法',
                'verbose_name_plural': '支援・受講方法一覧',
            },
        ),
        migrations.CreateModel(
            name='SupportStatusSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elem', models.CharField(max_length=32, verbose_name='支援状況')),
            ],
            options={
                'verbose_name': '支援状況',
                'verbose_name_plural': '支援状況一覧',
            },
        ),
        migrations.CreateModel(
            name='SupportThemeSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elem', models.CharField(max_length=32, verbose_name='支援テーマ')),
            ],
            options={
                'verbose_name': '支援テーマ',
                'verbose_name_plural': '支援テーマ一覧',
            },
        ),
        migrations.AlterField(
            model_name='office',
            name='address',
            field=models.CharField(max_length=64, null=True, verbose_name='事業所所在地'),
        ),
        migrations.AlterField(
            model_name='office',
            name='fax',
            field=models.CharField(max_length=16, null=True, verbose_name='FAX番号'),
        ),
        migrations.AlterField(
            model_name='office',
            name='latitude',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)], verbose_name='緯度'),
        ),
        migrations.AlterField(
            model_name='office',
            name='longitude',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)], verbose_name='経度'),
        ),
        migrations.AlterField(
            model_name='office',
            name='phone',
            field=models.CharField(max_length=16, null=True, verbose_name='電話番号'),
        ),
        migrations.AlterField(
            model_name='office',
            name='postal_code',
            field=models.CharField(max_length=16, null=True, verbose_name='郵便番号'),
        ),
        migrations.AlterField(
            model_name='office',
            name='town_code',
            field=models.CharField(max_length=16, null=True, verbose_name='事業所所在地の市区町村番号'),
        ),
        migrations.DeleteModel(
            name='SupportInfo',
        ),
    ]