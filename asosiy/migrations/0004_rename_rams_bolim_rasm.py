# Generated by Django 4.2 on 2023-04-10 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0003_mahsulot_sotuvchi'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bolim',
            old_name='rams',
            new_name='rasm',
        ),
    ]