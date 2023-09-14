# Generated by Django 4.2.5 on 2023-09-14 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_bid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Related_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='bid',
            options={'ordering': ['-amount']},
        ),
        migrations.AddField(
            model_name='card',
            name='related_products',
            field=models.ManyToManyField(to='main_app.related_product'),
        ),
    ]
