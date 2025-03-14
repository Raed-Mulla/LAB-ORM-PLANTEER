# Generated by Django 5.1.7 on 2025-03-10 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('about', models.TextField()),
                ('used_for', models.TextField()),
                ('image', models.ImageField(upload_to='image/')),
                ('category', models.CharField(choices=[('Annuals', 'Annual'), ('Herbs', 'Herb'), ('Shrubs', 'Shrub'), ('Trees', 'Tree'), ('Fruits', 'Fruit'), ('Vegetables', 'Vegetable')], max_length=1024)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
