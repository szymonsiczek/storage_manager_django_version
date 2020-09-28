# Generated by Django 3.1.1 on 2020-09-28 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('SO', 'Sound'), ('LI', 'Light'), ('ST', 'Stage'), ('PO', 'Power'), ('EX', 'Extra')], default='SO', max_length=2),
        ),
    ]
