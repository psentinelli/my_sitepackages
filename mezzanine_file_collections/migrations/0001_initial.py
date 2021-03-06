# Generated by Django 3.0.6 on 2020-05-26 13:53

from django.db import migrations, models
import django.db.models.deletion
import mezzanine.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0004_auto_20170411_0504'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaLibrary',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
            ],
            options={
                'verbose_name': 'Media Library',
                'verbose_name_plural': 'Media Libraries',
                'ordering': ('_order',),
            },
            bases=('pages.page', models.Model),
        ),
        migrations.CreateModel(
            name='MediaFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('file', mezzanine.core.fields.FileField(max_length=200, verbose_name='File')),
                ('title', models.CharField(blank=True, max_length=50, verbose_name='Title')),
                ('description', models.CharField(blank=True, max_length=1000, verbose_name='Description')),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='files', to='mezzanine_file_collections.MediaLibrary')),
            ],
            options={
                'verbose_name': 'Media File',
                'verbose_name_plural': 'Media Files',
                'ordering': ('_order',),
            },
        ),
    ]
