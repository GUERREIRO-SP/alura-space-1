# Generated by Django 5.0.7 on 2024-07-30 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0003_alter_fotografia_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('ESTRELA', 'Estrela'), ('GALÁXIA', 'Galáxia'), ('NEBULOSA', 'Nebulosa'), ('PLANETA', 'Planeta')], default='', max_length=100),
        ),
    ]
