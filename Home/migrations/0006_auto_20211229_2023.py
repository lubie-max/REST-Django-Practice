# Generated by Django 3.1.5 on 2021-12-29 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_auto_20211225_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadExcelFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_to', models.FileField(upload_to='excel')),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
