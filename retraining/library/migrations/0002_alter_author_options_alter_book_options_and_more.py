# Generated by Django 4.2.1 on 2023-06-05 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_create_book_author_and_reader_model'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AlterModelOptions(
            name='reader',
            options={'verbose_name': 'Читатель', 'verbose_name_plural': 'Читатели'},
        ),
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='reader',
            name='phone',
            field=models.CharField(max_length=12),
        ),
    ]
