# Generated by Django 4.1.4 on 2022-12-12 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pol', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='procedure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pol.procedure', verbose_name='С лучшим рейтингом'),
        ),
    ]
