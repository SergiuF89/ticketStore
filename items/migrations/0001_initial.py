# Generated by Django 3.1.2 on 2020-11-01 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('discount_price', models.FloatField(blank=True, null=True)),
                ('category', models.CharField(choices=[('T', 'Tickets')], max_length=2)),
                ('label', models.CharField(choices=[('P', 'success'), ('S', 'secondary'), ('D', 'danger')], max_length=1)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('genre', models.CharField(choices=[('1', 'Rock'), ('2', 'House'), ('3', 'Hip-Hop')], default=1, max_length=1)),
            ],
        ),
    ]
