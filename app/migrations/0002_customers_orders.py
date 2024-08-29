import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderdate', models.DateTimeField(auto_now_add=True)),
                ('shipper', models.CharField(max_length=20)),
                ('shipping_address', models.CharField(max_length=40)),
                ('shipping_country', models.CharField(max_length=20)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customers')),
            ],
        ),
    ]
