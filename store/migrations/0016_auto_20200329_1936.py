# Generated by Django 3.0.3 on 2020-03-29 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_sous_categorie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sous_categorie',
            name='photoSCat',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
