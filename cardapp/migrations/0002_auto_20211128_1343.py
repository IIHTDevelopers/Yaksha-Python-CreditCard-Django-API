# Generated by Django 3.1.7 on 2021-11-28 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carddetailsmodel',
            name='card_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cardtypesmodel',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customermodel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='limitincreaserequestmodel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='limitincreaserequestmodel',
            name='remark',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='requestmodel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='requestmodel',
            name='remark',
            field=models.CharField(max_length=100),
        ),
    ]