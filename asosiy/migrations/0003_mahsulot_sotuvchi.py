# Generated by Django 4.2 on 2023-04-10 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
        ('asosiy', '0002_mahsulot_holat'),
    ]

    operations = [
        migrations.AddField(
            model_name='mahsulot',
            name='sotuvchi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.profil'),
        ),
    ]