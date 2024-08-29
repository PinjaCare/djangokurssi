import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyname', models.CharField(default='firma', max_length=50)),
                ('contactname', models.CharField(default='firma', max_length=50)),
                ('address', models.CharField(default='firma', max_length=100)),
                ('phone', models.CharField(default='firma', max_length=20)),
                ('email', models.CharField(default='firma', max_length=50)),
                ('country', models.CharField(default='firma', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(default='laku', max_length=20)),
                ('packagesize', models.CharField(default=3, max_length=20)),
                ('unitprice', models.DecimalField(decimal_places=2, default=1.0, max_digits=8)),
                ('unitsinstock', models.IntegerField(default=3)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.supplier')),
            ],
        ),
    ]
