# Generated by Django 4.2.1 on 2023-06-25 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgu', '0008_alumno_apellido_alter_alumno_edad'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='diagnostico',
            field=models.FileField(default='default.png', upload_to='users/'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='identificacion',
            field=models.FileField(default='default.pdf', upload_to='users/'),
        ),
    ]