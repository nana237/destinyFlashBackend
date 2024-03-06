# Generated by Django 3.0.3 on 2020-03-31 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0036_auto_20200331_0023'),
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
        migrations.CreateModel(
            name='VERSEMENT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateVers', models.DateField()),
                ('typeVers', models.CharField(choices=[('B', 'Bancaire'), ('M', 'Mobile Money'), ('E', 'Espece')], default='E', max_length=1)),
                ('MontantVers', models.IntegerField()),
                ('statutVers', models.CharField(choices=[('E', 'En Attente'), ('EC', 'En Cour'), ('EF', 'Effectué'), ('T', 'Terminé')], default='E', max_length=2)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.CLIENT')),
                ('commande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.COMMANDE')),
            ],
        ),
    ]
