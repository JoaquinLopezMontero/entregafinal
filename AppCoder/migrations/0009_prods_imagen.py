# Generated by Django 4.1.5 on 2023-02-24 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0008_prods_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='prods',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='productospedidos'),
        ),
    ]
