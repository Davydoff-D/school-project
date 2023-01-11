# Generated by Django 3.2.16 on 2022-12-12 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning_materials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='group',
            field=models.ForeignKey(blank=True, help_text='Группа, к которой будет относиться пост', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='materials', to='learning_materials.group', verbose_name='Группа'),
        ),
    ]