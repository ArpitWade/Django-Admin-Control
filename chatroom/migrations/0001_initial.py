# Generated by Django 2.0.1 on 2023-06-29 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='layout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product', models.CharField(max_length=50)),
                ('Description', models.TextField()),
                ('Price', models.IntegerField()),
                ('ProductImage', models.ImageField(blank=True, null=True, upload_to='')),
                ('Offer', models.BooleanField(default=False)),
            ],
        ),
    ]
