# Generated by Django 3.0 on 2019-12-13 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='gender_options',
            field=models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER')], default=('male', 'MALE'), max_length=20),
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deposite', models.DecimalField(decimal_places=1, max_digits=20)),
                ('account_options', models.CharField(choices=[('savings', 'SAVINGS'), ('checkings', 'CHECKINGS'), ('business', 'BUSINESS')], default=('savings', 'SAVINGS'), max_length=20)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bank.Customer')),
            ],
        ),
    ]
