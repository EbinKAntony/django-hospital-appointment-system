# Generated by Django 2.2.1 on 2019-06-12 00:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=75, verbose_name='Şehir Adı')),
            ],
            options={
                'verbose_name': 'Şehirler',
                'verbose_name_plural': 'Şehirler',
            },
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('county_name', models.CharField(max_length=75, verbose_name='İlçe')),
                ('city_of_county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='randevu.City', verbose_name='Şehir')),
            ],
            options={
                'verbose_name': 'İlçeler',
                'verbose_name_plural': 'İlçeler',
            },
        ),
        migrations.CreateModel(
            name='Hospitals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=75, verbose_name='Hastane Adı')),
                ('begin_time', models.TimeField(verbose_name='Açılış Saati')),
                ('end_time', models.TimeField(verbose_name='Kapanış Saati')),
                ('hospital_telephone', models.CharField(max_length=20, verbose_name='Telefon No')),
                ('hospital_address', models.TextField(max_length=200, verbose_name='Adres')),
                ('county_of_hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='randevu.County', verbose_name='İlçe')),
            ],
            options={
                'verbose_name': 'Hastaneler',
                'verbose_name_plural': 'Hastaneler',
            },
        ),
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('patient_tc_no', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='Tc No')),
                ('patient_name', models.CharField(max_length=25, verbose_name='Adı')),
                ('patient_surname', models.CharField(max_length=25, verbose_name='Soyadı')),
                ('blood_group_of_patient', models.CharField(choices=[('0 Rh-', '0 Rh-'), ('0 Rh+', '0 Rh+'), ('A Rh-', 'A Rh-'), ('A Rh+', 'A Rh+'), ('B Rh-', 'B Rh-'), ('B Rh+', 'B Rh+'), ('AB Rh-', 'AB Rh-'), ('AB Rh+', 'AB Rh+')], max_length=5, verbose_name='Kan Grubu')),
                ('mother_name_of_patient', models.CharField(max_length=15, verbose_name='Anne Adı')),
                ('father_name_of_patient', models.CharField(max_length=15, verbose_name='Baba Adı')),
                ('telephone_of_patient', models.CharField(max_length=20, verbose_name='Telefonu')),
                ('e_mail_of_patient', models.CharField(max_length=50, verbose_name='E-Mail')),
                ('patient_place_of_birth', models.CharField(max_length=15, verbose_name='Doğum Yeri')),
                ('patient_date_of_birth', models.DateField(default=datetime.date.today, verbose_name='Doğum Tarihi')),
                ('gender_of_patient', models.CharField(choices=[('Erkek', 'Erkek'), ('Kadın', 'Kadın')], max_length=5, verbose_name='Cinsiyet')),
                ('password_of_patient', models.CharField(max_length=16, verbose_name='Parola')),
            ],
            options={
                'verbose_name': 'Hastalar',
                'verbose_name_plural': 'Hastalar',
            },
        ),
        migrations.CreateModel(
            name='Polyclinics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polyclinic_name', models.CharField(max_length=50, verbose_name='Poliklinik Adı')),
                ('hospital_of_polyclinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='randevu.Hospitals', verbose_name='Hastane')),
            ],
            options={
                'verbose_name': 'Poliklinikler',
                'verbose_name_plural': 'Poliklinikler',
            },
        ),
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('dr_tc_no', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='Tc No')),
                ('dr_name', models.CharField(max_length=25, verbose_name='Adı')),
                ('dr_surname', models.CharField(max_length=25, verbose_name='Soyadı')),
                ('telephone_of_dr', models.CharField(max_length=20, verbose_name='Telefon No')),
                ('expertise_of_dr', models.CharField(max_length=25, verbose_name='Uzmanlık')),
                ('dr_place_of_birth', models.CharField(max_length=15, verbose_name='Dogum Yeri')),
                ('dr_date_of_birth', models.DateField(verbose_name='Doğum Tarihi')),
                ('gender_of_dr', models.CharField(choices=[('Erkek', 'Erkek'), ('Kadın', 'Kadın')], max_length=5, verbose_name='Cinsiyet')),
                ('polyclinic_of_doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='randevu.Polyclinics', verbose_name='Poliklinik')),
            ],
            options={
                'verbose_name': 'Doktorlar',
                'verbose_name_plural': 'Doktorlar',
            },
        ),
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_appointment', models.DateField(verbose_name='Randevu Tarihi')),
                ('begin_time_of_appointment', models.TimeField(verbose_name='Başlangıç Zamanı')),
                ('dr_of_appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='randevu.Doctors', verbose_name='Doktor')),
                ('patient_of_appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='randevu.Patients', verbose_name='Hasta')),
            ],
            options={
                'verbose_name': 'Randevular',
                'verbose_name_plural': 'Randevular',
            },
        ),
    ]
