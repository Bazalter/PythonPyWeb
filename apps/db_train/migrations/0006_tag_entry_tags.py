# Generated by Django 4.2.5 on 2024-03-28 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_train', '0005_entry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='tags',
            field=models.ManyToManyField(related_name='entries', to='db_train.tag'),
        ),
    ]
