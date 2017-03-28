# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 15:36
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Backtests',
            fields=[
                ('buid', models.CharField(max_length=32, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(message='Only alphanumeric characters are allowed', regex='^[0-9a-z]*$')])),
                ('trade_frequency', models.CharField(choices=[('daily', 'daily'), ('weekly', 'weekly'), ('minute', 'minute'), ('hourly', 'hourly'), ('monthly', 'monthly')], default='daily', max_length=10)),
                ('shares', models.PositiveIntegerField(blank=True, null=True)),
                ('pnl', models.FloatField(null=True)),
                ('volatility', models.FloatField(null=True)),
                ('sharpe_ratio', models.FloatField(null=True)),
                ('sortino_ratio', models.FloatField(null=True)),
                ('max_drawdown', models.FloatField(null=True)),
                ('winning_rate', models.FloatField(null=True)),
                ('losing_rate', models.FloatField(null=True)),
                ('start', models.DateTimeField(null=True)),
                ('end', models.DateTimeField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Backtests',
            },
        ),
        migrations.CreateModel(
            name='Indicators',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abbreviation', models.CharField(blank=True, max_length=10, unique=True)),
                ('name', models.CharField(blank=True, max_length=50, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Indicators',
            },
        ),
        migrations.CreateModel(
            name='Strategy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('strategy', models.CharField(blank=True, max_length=999, null=True)),
                ('trade_frequency', models.CharField(choices=[('daily', 'daily'), ('weekly', 'weekly'), ('minute', 'minute'), ('hourly', 'hourly'), ('monthly', 'monthly')], default='daily', max_length=10)),
                ('shares', models.PositiveIntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Strategies',
            },
        ),
        migrations.CreateModel(
            name='Ticker',
            fields=[
                ('symbol', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('exchange', models.CharField(choices=[('nse', 'nse')], default='nse', max_length=6)),
                ('uin', models.CharField(blank=True, max_length=20, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='strategy',
            name='ticker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='processor.Ticker'),
        ),
        migrations.AddField(
            model_name='strategy',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='backtests',
            name='strategy_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='processor.Strategy'),
        ),
        migrations.AddField(
            model_name='backtests',
            name='ticker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='processor.Ticker'),
        ),
        migrations.AddField(
            model_name='backtests',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
