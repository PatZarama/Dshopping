from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Creation date')),
                ('modify_date', models.DateField(auto_now=True, verbose_name='Modify date')),
                ('delete_date', models.DateField(auto_now=True, verbose_name='Delete date')),
                ('title', models.CharField(max_length=100, verbose_name='Category name')),
                ('description', models.CharField(max_length=100, verbose_name='description')),
                ('status', models.CharField(max_length=100, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='clients',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Creation date')),
                ('modify_date', models.DateField(auto_now=True, verbose_name='Modify date')),
                ('delete_date', models.DateField(auto_now=True, verbose_name='Delete date')),
                ('id_client', models.CharField(max_length=10, unique=True, verbose_name='Id Client')),
                ('first_name', models.CharField(max_length=100, verbose_name='First name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last name')),
                ('id_gender', models.CharField(max_length=1, verbose_name='Gender')),
                ('phone', models.CharField(max_length=10, unique=True, verbose_name='phone')),
                ('email', models.EmailField(max_length=150, verbose_name='E-mail')),
                ('password', models.CharField(max_length=15, verbose_name='Password')),
                ('id_country', models.CharField(max_length=20, verbose_name='Id Country')),
                ('image', models.ImageField(blank=True, null=True, upload_to='authors/', verbose_name='Author image')),
                ('message', models.TextField(max_length=10, verbose_name='Status')),
                ('credit_card_number', models.TextField(max_length=15, verbose_name='Number credit')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
        migrations.CreateModel(
            name='country',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Creation date')),
                ('modify_date', models.DateField(auto_now=True, verbose_name='Modify date')),
                ('delete_date', models.DateField(auto_now=True, verbose_name='Delete date')),
                ('title', models.CharField(max_length=100, verbose_name='Country name')),
                ('abreviation', models.CharField(max_length=100, verbose_name='Abreviation')),
                ('status', models.CharField(max_length=100, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='gender',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Creation date')),
                ('modify_date', models.DateField(auto_now=True, verbose_name='Modify date')),
                ('delete_date', models.DateField(auto_now=True, verbose_name='Delete date')),
                ('title', models.CharField(max_length=100, verbose_name='Country name')),
                ('description', models.CharField(max_length=100, verbose_name='description')),
                ('status', models.CharField(max_length=100, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Gender',
                'verbose_name_plural': 'Genders',
            },
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Creation date')),
                ('modify_date', models.DateField(auto_now=True, verbose_name='Modify date')),
                ('delete_date', models.DateField(auto_now=True, verbose_name='Delete date')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Prodcut photo')),
                ('quantity', models.CharField(max_length=100, verbose_name='Quantity')),
                ('status', models.CharField(max_length=100, verbose_name='Status')),
                ('id_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.category')),
                ('id_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.country')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='shopping',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Creation date')),
                ('modify_date', models.DateField(auto_now=True, verbose_name='Modify date')),
                ('delete_date', models.DateField(auto_now=True, verbose_name='Delete date')),
                ('shopping_date', models.CharField(max_length=100, verbose_name='Shopping Date')),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.clients')),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.products')),
            ],
            options={
                'verbose_name': 'Shopping',
                'verbose_name_plural': 'Shoppings',
            },
        ),
    ]
