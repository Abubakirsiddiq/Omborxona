# Generated by Django 4.0.3 on 2022-06-14 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_remove_ombor_nom_remove_ombor_tel_raqam_ombor_dokon_and_more'),
        ('asosiy', '0002_remove_client_tel_raqam_client_tel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='ombor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='userapp.ombor'),
        ),
        migrations.AlterField(
            model_name='mahsulot',
            name='ombor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='userapp.ombor'),
        ),
    ]
