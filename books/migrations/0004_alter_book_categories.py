# Generated by Django 3.2 on 2021-04-22 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_isbn_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, to='books.Category'),
        ),
    ]