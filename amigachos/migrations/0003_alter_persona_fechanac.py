# Generated by Django 4.0.6 on 2022-08-19 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amigachos', '0002_persona_fechacreacion_alter_persona_fechanac'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='fechaNac',
            field=models.DateTimeField(blank=True),
        ),
    ]
