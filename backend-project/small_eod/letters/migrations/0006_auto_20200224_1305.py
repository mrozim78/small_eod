# Generated by Django 3.0.3 on 2020-02-24 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0007_auto_20200221_1956'),
        ('cases', '0007_auto_20200221_1956'),
        ('letters', '0005_auto_20200221_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='case',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cases.Case', verbose_name='Case'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='institution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='institutions.Institution', verbose_name='Institution'),
        ),
    ]
