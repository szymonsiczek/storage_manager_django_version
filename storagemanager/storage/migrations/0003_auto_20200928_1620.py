# Generated by Django 3.1.1 on 2020-09-28 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0002_auto_20200928_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('Sound', 'Sound'), ('Light', 'Light'), ('Stage', 'Stage'), ('Power', 'Power'), ('Extra', 'Extra'), ('bonus', 'Bonus')], default='Sound', max_length=10),
        ),
    ]
