# Generated by Django 5.0.6 on 2024-06-06 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0002_alter_plan_cost_alter_plan_validity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='cost',
            field=models.IntegerField(choices=[(499, 499), (299, 299), (199, 199)]),
        ),
        migrations.AlterField(
            model_name='plan',
            name='validity',
            field=models.IntegerField(choices=[(365, 365), (180, 180), (90, 90)]),
        ),
    ]