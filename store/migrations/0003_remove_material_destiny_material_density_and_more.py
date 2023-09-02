# Generated by Django 4.2.4 on 2023-09-02 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_preparedpurchase_title_alter_consult_purchase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='destiny',
        ),
        migrations.AddField(
            model_name='material',
            name='density',
            field=models.PositiveIntegerField(default=0, verbose_name='density in kg/m3 units'),
        ),
        migrations.AlterField(
            model_name='consult',
            name='comment',
            field=models.TextField(default='Enter your comment here', max_length=512, verbose_name='consultant comment'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='address',
            field=models.TextField(max_length=512, verbose_name='address inside Westland'),
        ),
        migrations.AlterIndexTogether(
            name='preparedpurchase',
            index_together={('color', 'material', 'size')},
        ),
    ]