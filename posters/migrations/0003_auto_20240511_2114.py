# Generated by Django 3.0.1 on 2024-05-11 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posters', '0002_auto_20240419_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuantityColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_option', models.CharField(choices=[('Color', 'Color'), ('Black & White', 'Black & White')], default='Color', max_length=80)),
            ],
        ),
        migrations.AddField(
            model_name='poster',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
