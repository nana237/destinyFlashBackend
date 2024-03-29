# Generated by Django 3.0.3 on 2020-04-22 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0046_auto_20200422_2157'),
    ]

    operations = [
        
        migrations.CreateModel(
            name='DET_COM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qteCom', models.IntegerField()),
                ('couleurCom', models.CharField(blank=True, max_length=50, null=True)),
                ('tailleCom', models.CharField(blank=True, max_length=50, null=True)),
                ('prixCom', models.IntegerField(blank=True, null=True)),
                ('autreDetailCom', models.CharField(blank=True, max_length=256, null=True)),
                ('article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.ARTICLE')),
                ('commande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.COMMANDE')),
            ],
        ),
        migrations.AlterField(
            model_name='commande',
            name='articles',
            field=models.ManyToManyField(blank=True, null=True, through='store.DET_COM', to='store.ARTICLE'),
        ),
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
        
    ]
