# Generated by Django 4.2.6 on 2023-10-29 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=15)),
                ('amount', models.IntegerField(default=0)),
                ('used_amount', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('Yangi', 'New'), ('Moderatsiyada', 'Moderation'), ('Tasdiqlangan', 'Approved'), ('Bekor qilingan', 'Canceled')], default='Yangi', max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
