# Generated by Django 3.1.1 on 2020-10-07 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20201003_1953'),
    ]

    operations = [
        migrations.CreateModel(
            name='list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('parent_board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.board')),
            ],
        ),
    ]
