# Generated by Django 4.0.3 on 2022-06-16 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userapp', '0002_remove_ombor_nom_remove_ombor_tel_raqam_ombor_dokon_and_more'),
        ('asosiy', '0003_alter_client_ombor_alter_mahsulot_ombor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sana', models.DateTimeField(auto_now_add=True)),
                ('miqdor', models.PositiveIntegerField()),
                ('umumiy', models.PositiveIntegerField()),
                ('tolandi', models.PositiveIntegerField()),
                ('nasiya', models.PositiveIntegerField()),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='asosiy.client')),
                ('mahsulot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='asosiy.mahsulot')),
                ('ombor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='userapp.ombor')),
            ],
        ),
    ]
