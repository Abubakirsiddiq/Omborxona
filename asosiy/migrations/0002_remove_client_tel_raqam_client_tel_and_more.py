# Generated by Django 4.0.3 on 2022-06-14 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_remove_ombor_nom_remove_ombor_tel_raqam_ombor_dokon_and_more'),
        ('asosiy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='tel_raqam',
        ),
        migrations.AddField(
            model_name='client',
            name='tel',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='client',
            name='dokon',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='client',
            name='ism',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='client',
            name='manzil',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='client',
            name='ombor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.ombor'),
        ),
        migrations.AlterField(
            model_name='mahsulot',
            name='brend',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='mahsulot',
            name='miqdor',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='mahsulot',
            name='nom',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='mahsulot',
            name='ombor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.ombor'),
        ),
    ]
