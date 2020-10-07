# Generated by Django 3.1.1 on 2020-10-07 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
                ('due_date', models.DateTimeField()),
                ('parent_board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.list')),
            ],
        ),
    ]