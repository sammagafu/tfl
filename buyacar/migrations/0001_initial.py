# Generated by Django 3.2 on 2021-10-07 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BuyACar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='car/cover/%Y/%m/%d', verbose_name='Cover Image')),
                ('price', models.IntegerField(default=10, help_text='Enter price in USD', verbose_name='Cars Price')),
                ('car_status', models.CharField(choices=[('Used', 'Used'), ('New', 'New')], default='Used', max_length=50, verbose_name='Car status')),
                ('model', models.CharField(max_length=50, verbose_name='Car Model')),
                ('trans', models.CharField(choices=[('AT', 'AUTOMATIC'), ('Mn', 'Manual')], max_length=2, verbose_name='Transmision')),
                ('fuel', models.CharField(choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Gas', 'Gas'), ('Electric', 'Electric'), ('Hibrid', 'Hibrid')], max_length=12, verbose_name='Fuel')),
                ('mileage', models.IntegerField(verbose_name='Milage')),
                ('engine', models.IntegerField(verbose_name='Engine size')),
                ('registered', models.IntegerField(verbose_name='Registered Year')),
                ('doors', models.IntegerField(verbose_name='Doors')),
                ('seats', models.IntegerField(verbose_name='Seats')),
                ('passenger', models.IntegerField(verbose_name='Passengers')),
                ('body', models.IntegerField(verbose_name='Body')),
                ('hand', models.CharField(choices=[('Left', 'Left'), ('Right', 'Right'), ('Default', 'Defaut')], max_length=12, verbose_name='Driving Hand')),
                ('drive', models.CharField(choices=[('2WD', '2WD'), ('4WD', '4WD'), ('AWD', 'AWD')], max_length=12, verbose_name='Drive')),
                ('available', models.BooleanField(default=True, verbose_name='Car is available')),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
            },
        ),
        migrations.CreateModel(
            name='CarColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=30, verbose_name='Car Color')),
                ('slug', models.SlugField(blank=True, editable=False, null=True, verbose_name='slug')),
            ],
        ),
        migrations.CreateModel(
            name='CarFeatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, editable=False, null=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Feature',
                'verbose_name_plural': 'Features',
            },
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=120, verbose_name='car brand name')),
                ('logo', models.ImageField(help_text='Height and width must be 100px x 100px', upload_to='car/logo/')),
                ('slug', models.SlugField(blank=True, editable=False, null=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Car Manufacture',
                'verbose_name_plural': 'Cars Manufactures',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='If its a car, bike or Tricycle', max_length=120)),
                ('slug', models.SlugField(blank=True, editable=False, null=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='CarImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='car/images/%Y/%m/%d', verbose_name='Other Images')),
                ('car', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='buyacar.buyacar')),
            ],
        ),
        migrations.AddField(
            model_name='buyacar',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyacar.carmodel', verbose_name='Brand Name'),
        ),
        migrations.AddField(
            model_name='buyacar',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='buyacar.category', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='buyacar',
            name='color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='buyacar.carcolor', verbose_name='Car color'),
        ),
        migrations.AddField(
            model_name='buyacar',
            name='features',
            field=models.ManyToManyField(to='buyacar.CarFeatures', verbose_name='features'),
        ),
    ]
