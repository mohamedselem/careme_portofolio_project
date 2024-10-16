# Generated by Django 5.0.1 on 2024-04-19 12:57

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('appointment_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('symptom_type', models.CharField(default='General', max_length=255)),
                ('symptom_description', models.TextField(default='How Exactly do you feel')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Completed', 'Completed'), ('Canceled', 'Canceled')], default='Pending', max_length=10)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.patient')),
                ('specialist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.specialist')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('notification_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('notification_type', models.CharField(max_length=255)),
                ('is_read', models.BooleanField(default=False)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_notifications', to='profiles.user')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_notifications', to='profiles.user')),
            ],
        ),
    ]
