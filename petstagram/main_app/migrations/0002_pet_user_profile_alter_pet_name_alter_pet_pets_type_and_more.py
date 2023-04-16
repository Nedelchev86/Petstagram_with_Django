# Generated by Django 4.2 on 2023-04-15 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='user_profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.profile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pet',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='pet',
            name='pets_type',
            field=models.CharField(choices=[('Cat', 'Cat'), ('Dog', 'Dog'), ('Bunny', 'Bunny'), ('Fish', 'Fish'), ('Other', 'Other')], max_length=5),
        ),
        migrations.AlterUniqueTogether(
            name='pet',
            unique_together={('user_profile', 'name')},
        ),
    ]