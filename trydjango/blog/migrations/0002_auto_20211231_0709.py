# Generated by Django 3.2.9 on 2021-12-31 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aritcle',
            old_name='discount',
            new_name='active',
        ),
        migrations.RemoveField(
            model_name='aritcle',
            name='price',
        ),
        migrations.RemoveField(
            model_name='aritcle',
            name='summury',
        ),
        migrations.AlterField(
            model_name='aritcle',
            name='discription',
            field=models.CharField(max_length=1000000),
        ),
    ]