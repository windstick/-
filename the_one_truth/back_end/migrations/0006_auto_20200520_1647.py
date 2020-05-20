# Generated by Django 3.0.5 on 2020-05-20 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('back_end', '0005_auto_20200519_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game_clue',
            name='script_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='back_end.script'),
        ),
        migrations.AlterField(
            model_name='game_room',
            name='script_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='back_end.script'),
        ),
    ]
