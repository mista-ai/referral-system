# Generated by Django 5.0.6 on 2024-06-07 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('referral_system', '0002_rename_expires_at_referralcode_expiry_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='referralcode',
            old_name='expiry_date',
            new_name='expiration_date',
        ),
        migrations.AlterField(
            model_name='referralcode',
            name='code',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
