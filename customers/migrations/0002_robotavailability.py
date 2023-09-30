# Generated by Django 4.2.5 on 2023-09-28 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('robots', '0002_robot_quantity'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RobotAvailability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.BooleanField(default=False)),
                ('queued_for_notification', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customers.customer')),
                ('robot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='robots.robot')),
            ],
        ),
    ]
