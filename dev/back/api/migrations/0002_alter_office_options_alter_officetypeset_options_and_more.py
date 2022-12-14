# Generated by Django 4.1.3 on 2022-11-08 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='office',
            options={'verbose_name': '事業所', 'verbose_name_plural': '事業所一覧'},
        ),
        migrations.AlterModelOptions(
            name='officetypeset',
            options={'verbose_name': '事業所種別', 'verbose_name_plural': '事業所種別一覧'},
        ),
        migrations.RenameField(
            model_name='office',
            old_name='company_name',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='office',
            old_name='fax_number',
            new_name='fax',
        ),
        migrations.RenameField(
            model_name='office',
            old_name='phone_number',
            new_name='phone',
        ),
        migrations.AddField(
            model_name='office',
            name='foundation_date',
            field=models.DateField(null=True, verbose_name='設立年月日'),
        ),
        migrations.AddField(
            model_name='office',
            name='number_of_employees',
            field=models.IntegerField(null=True, verbose_name='従業員人数'),
        ),
        migrations.AlterField(
            model_name='office',
            name='capacity_employment',
            field=models.IntegerField(null=True, verbose_name='定員'),
        ),
        migrations.AlterField(
            model_name='office',
            name='id',
            field=models.CharField(help_text='介護保険事業所番号＠介護サービス分類コード\u3000の半角文字列で構成されます。', max_length=32, verbose_name='識別子'),
        ),
        migrations.AlterField(
            model_name='office',
            name='url',
            field=models.CharField(max_length=64, null=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='officetypeset',
            name='elem',
            field=models.CharField(max_length=32, verbose_name='事業所種別'),
        ),
        migrations.CreateModel(
            name='SupportInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_date', models.DateField(null=True, verbose_name='申込日')),
                ('visit_date', models.DateField(null=True, verbose_name='訪問日')),
                ('implementation_date', models.DateField(null=True, verbose_name='実施日')),
                ('company', models.OneToOneField(db_column='company', null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.office', verbose_name='支援事業所法人名')),
            ],
            options={
                'verbose_name': '支援情報',
                'verbose_name_plural': '支援情報一覧',
            },
        ),
    ]
