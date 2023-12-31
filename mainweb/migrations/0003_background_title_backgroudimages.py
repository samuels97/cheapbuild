# Generated by Django 4.2.3 on 2023-08-02 15:54

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mainweb', '0002_career_testimony_alter_banners_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='background',
            name='title',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.CreateModel(
            name='backgroudImages',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='backc')),
                ('title', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='mainweb.background')),
            ],
            options={
                'verbose_name_plural': '01. Back Images',
            },
        ),
    ]
