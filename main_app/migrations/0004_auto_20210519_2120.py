# Generated by Django 3.2.3 on 2021-05-19 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_review_game'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateField(verbose_name='Date Reviewed'),
        ),
        migrations.AddField(
            model_name='game',
            name='stores',
            field=models.ManyToManyField(to='main_app.Store'),
        ),
    ]
