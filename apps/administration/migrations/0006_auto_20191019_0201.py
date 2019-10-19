from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0005_auto_20191019_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='credit_card_number',
            field=models.CharField(max_length=15, verbose_name='Number credit'),
        ),
    ]
