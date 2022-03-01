# Generated by Django 3.2.5 on 2021-09-16 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210907_0857'),
        ('projects', '0004_project_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['created']},
        ),
        migrations.AddField(
            model_name='review',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('owner', 'project')},
        ),
    ]
