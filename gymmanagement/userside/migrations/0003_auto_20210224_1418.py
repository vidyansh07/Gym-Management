# Generated by Django 3.1.5 on 2021-02-24 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userside', '0002_auto_20210224_0956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_type',
            name='id',
        ),
        migrations.AddField(
            model_name='user_type',
            name='type_id',
            field=models.IntegerField(auto_created=True, default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='attendance_master',
            name='time_in',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='attendance_master',
            name='time_out',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='user_master',
            name='gender',
            field=models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=1),
        ),
        migrations.AlterField(
            model_name='user_master',
            name='mname',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='user_master',
            name='type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userside.user_type'),
        ),
    ]