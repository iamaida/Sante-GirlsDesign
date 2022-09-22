# Generated by Django 4.1.1 on 2022-09-22 02:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('especialidad_id', models.AutoField(primary_key=True, serialize=False)),
                ('especialidad_name', models.CharField(max_length=100, verbose_name='especialidad')),
            ],
        ),
        migrations.CreateModel(
            name='HistoriaClinica',
            fields=[
                ('historiaclinica_id', models.AutoField(primary_key=True, serialize=False)),
                ('diagnostico', models.CharField(max_length=300, verbose_name='diagnostico')),
                ('evolucion', models.CharField(max_length=3000, verbose_name='evolucion')),
                ('sugerencias_cuidado', models.CharField(max_length=3000, verbose_name='sugerencias_cuidado')),
            ],
        ),
        migrations.CreateModel(
            name='SignosVitales',
            fields=[
                ('codigo_sv', models.AutoField(primary_key=True, serialize=False)),
                ('oximetria', models.CharField(max_length=25, verbose_name='oximetria')),
                ('frecuencia_respiratoria', models.CharField(max_length=25, verbose_name='frecuencia_respiratoria')),
                ('frecuencia_cardiaca', models.CharField(max_length=25, verbose_name='frecuencia_cardiaca')),
                ('temperatura', models.CharField(max_length=25, verbose_name='temperatura')),
                ('presion_arterial', models.CharField(max_length=25, verbose_name='presion_arterial')),
                ('glicemia', models.CharField(max_length=25, verbose_name='glicemia')),
                ('historiaclinica_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='signosvitales', to='authApp.historiaclinica')),
            ],
        ),
        migrations.CreateModel(
            name='PersonalSalud',
            fields=[
                ('ps_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='apellido')),
                ('tipo_documento', models.CharField(max_length=10, verbose_name='tipo_documento')),
                ('numero_documento', models.CharField(max_length=100, verbose_name='numero_documento')),
                ('fecha_nacimiento', models.DateField(verbose_name='fecha_nacimiento')),
                ('genero', models.CharField(max_length=20, verbose_name='genero')),
                ('telefono', models.CharField(max_length=15, verbose_name='telefono')),
                ('correo_electronico', models.EmailField(max_length=100, verbose_name='correo_electronico')),
                ('registro', models.CharField(max_length=25, verbose_name='registro')),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personalsalud', to=settings.AUTH_USER_MODEL)),
                ('especialidad_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personalsalud', to='authApp.especialidad')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('paciente_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='apellido')),
                ('tipo_documento', models.CharField(max_length=10, verbose_name='tipo_documento')),
                ('numero_documento', models.CharField(max_length=100, verbose_name='numero_documento')),
                ('fecha_nacimiento', models.DateField(verbose_name='fecha_nacimiento')),
                ('genero', models.CharField(max_length=20, verbose_name='genero')),
                ('telefono', models.CharField(max_length=15, verbose_name='telefono')),
                ('correo_electronico', models.EmailField(max_length=100, verbose_name='correo_electronico')),
                ('direccion', models.CharField(max_length=150, verbose_name='direccion')),
                ('ciudad', models.CharField(max_length=150, verbose_name='ciudad')),
                ('latitud_longitud', models.CharField(max_length=300, verbose_name='latitud_longitud')),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paciente', to=settings.AUTH_USER_MODEL)),
                ('ps_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paciente', to='authApp.personalsalud')),
            ],
        ),
        migrations.AddField(
            model_name='historiaclinica',
            name='paciente_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historiaclinica', to='authApp.paciente'),
        ),
        migrations.AddField(
            model_name='historiaclinica',
            name='ps_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historiaclinica', to='authApp.personalsalud'),
        ),
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('familiar_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='apellido')),
                ('tipo_documento', models.CharField(max_length=10, verbose_name='tipo_documento')),
                ('numero_documento', models.CharField(max_length=100, verbose_name='numero_documento')),
                ('parentesco', models.CharField(max_length=50, verbose_name='parentesco')),
                ('genero', models.CharField(max_length=20, verbose_name='genero')),
                ('telefono', models.CharField(max_length=15, verbose_name='telefono')),
                ('correo_electronico', models.EmailField(max_length=100, verbose_name='correo_electronico')),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='familiar', to=settings.AUTH_USER_MODEL)),
                ('paciente_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='familiar', to='authApp.paciente')),
            ],
        ),
    ]
