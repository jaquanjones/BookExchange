# Generated by Django 3.0.3 on 2020-10-16 18:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookMng', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('web', models.URLField(max_length=300)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('publishdate', models.DateField(auto_now=True)),
                ('picture', models.FileField(upload_to='bookEx/static/uploads')),
                ('pic_path', models.CharField(blank=True, editable=False, max_length=300)),
                ('username', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
