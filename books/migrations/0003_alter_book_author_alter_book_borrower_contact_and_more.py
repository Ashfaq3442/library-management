# Generated by Django 5.1.1 on 2024-10-06 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_borrower_address_book_borrower_contact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='book',
            name='borrower_contact',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='borrower_name',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=225),
        ),
    ]
