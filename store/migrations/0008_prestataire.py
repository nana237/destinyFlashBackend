# Generated by Django 3.0.3 on 2020-03-29 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20200329_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='PRESTATAIRE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomP', models.CharField(max_length=100)),
                ('prenomP', models.CharField(max_length=100)),
                ('dateNaissP', models.DateField()),
                ('emailP', models.EmailField(max_length=254)),
                ('sexeP', models.CharField(choices=[('M', 'Masculin'), ('F', 'Feminin')], default='M', max_length=1)),
                ('adresseP', models.CharField(max_length=100)),
                ('villeP', models.CharField(max_length=100)),
                ('quartierP', models.CharField(max_length=100)),
                ('numCNI_P', models.CharField(max_length=25, unique=True)),
                ('telP', models.IntegerField()),
                ('loginP', models.CharField(max_length=100)),
                ('motDePassP', models.CharField(max_length=50)),
            ],
        ),
    ]