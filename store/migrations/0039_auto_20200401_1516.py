# Generated by Django 3.0.3 on 2020-04-01 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0038_auto_20200331_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caracteristique',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.ARTICLE'),
        ),
        migrations.AlterField(
            model_name='commande',
            name='articles',
            field=models.ManyToManyField(to='store.ARTICLE'),
        ),
        migrations.AlterField(
            model_name='panier',
            name='articles',
            field=models.ManyToManyField(to='store.ARTICLE'),
        ),
    ]
