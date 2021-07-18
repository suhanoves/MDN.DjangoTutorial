# Generated by Django 3.2.5 on 2021-07-18 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_book_summary'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'verbose_name': 'Экземпляр книги', 'verbose_name_plural': 'Экземпляры книг'},
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(related_name='books', related_query_name='book', to='catalog.Author'),
        ),
        migrations.AddField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(help_text='Выберите жанры, подходящие для этой книги', related_name='books', related_query_name='book', to='catalog.Genre'),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instances', related_query_name='instance', to='catalog.book'),
        ),
    ]
