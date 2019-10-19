from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0002_auto_20191019_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopping',
            name='shopping_date',
            field=models.DateField(auto_now=True, verbose_name='Shopping date'),
        ),
    ]
