# Generated by Django 3.1.1 on 2020-10-04 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blognews',
            name='name',
            field=models.CharField(default=True, max_length=250),
            preserve_default=False,
        ),
    ]
