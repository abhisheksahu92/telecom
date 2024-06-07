# Generated by Django 5.0.6 on 2024-06-06 14:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('plan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('renewal_date', models.DateField(blank=True, null=True)),
                ('existing_plan_name', models.CharField(blank=True, max_length=50, null=True)),
                ('new_plan_name', models.CharField(blank=True, max_length=50, null=True)),
                ('plan_status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.plan')),
            ],
        ),
    ]