# Generated by Django 2.0.6 on 2018-06-19 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('multi_table', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('place_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='multi_table.Place')),
            ],
            bases=('multi_table.place',),
        ),
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='supplier',
            name='customers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplier_by_customer', to='multi_table.Place'),
        ),
    ]
