# Generated by Django 4.2.5 on 2023-09-29 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('robots', '0002_robot_quantity'),
        ('customers', '0002_robotavailability'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='robotavailability',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='robotavailability',
            name='queued_for_notification',
        ),
        migrations.AlterField(
            model_name='robotavailability',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='robotavailability',
            name='robot',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='availability', to='robots.robot'),
        ),
        migrations.CreateModel(
            name='RobotRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=2)),
                ('version', models.CharField(max_length=2)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customers.customer')),
            ],
        ),
    ]
