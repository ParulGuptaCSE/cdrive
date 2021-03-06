# Generated by Django 3.0.3 on 2020-03-01 17:15

from django.db import migrations, models
import django.db.models.deletion
import drive_api.models

def create_home(apps, schema_editor):
    CDriveFolder = apps.get_model('drive_api', 'CDriveFolder')
    home_folder = CDriveFolder(
        name = 'users',
        parent = None,
        owner = None
    )
    home_folder.save()

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services_api', '0001_initial'),
        ('apps_api', '0001_initial'),
        ('user_mgmt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CDriveFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('cdrive_file', models.FileField(upload_to=drive_api.models.file_path)),
                ('size', models.IntegerField()),
                ('is_public', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cdrivefile_owner', to='user_mgmt.CDriveUser')),
            ],
        ),
        migrations.CreateModel(
            name='CDriveFolder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('is_public', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cdrivefolder_owner', to='user_mgmt.CDriveUser')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cdrivefolder_parent', to='drive_api.CDriveFolder')),
            ],
        ),
        migrations.CreateModel(
            name='HostedServiceFolderPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(choices=[('V', 'View'), ('E', 'Edit')], max_length=1)),
                ('cdrive_folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hostedservicefolderpermission_folder', to='drive_api.CDriveFolder')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hostedservicefolderpermission_service', to='services_api.HostedService')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hostedservicefolderpermission_user', to='user_mgmt.CDriveUser')),
            ],
        ),
        migrations.CreateModel(
            name='HostedServiceFilePermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(choices=[('V', 'View'), ('E', 'Edit')], max_length=1)),
                ('cdrive_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hostedservicefilepermission_file', to='drive_api.CDriveFile')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hostedservicefilepermission_service', to='services_api.HostedService')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hostedservicefilepermission_user', to='user_mgmt.CDriveUser')),
            ],
        ),
        migrations.CreateModel(
            name='FolderPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(choices=[('V', 'View'), ('E', 'Edit')], max_length=1)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='folderpermission_app', to='apps_api.CDriveApplication')),
                ('cdrive_folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='folderpermission_folder', to='drive_api.CDriveFolder')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='folderpermission_user', to='user_mgmt.CDriveUser')),
            ],
        ),
        migrations.CreateModel(
            name='FilePermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(choices=[('V', 'View'), ('E', 'Edit')], max_length=1)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filepermission_app', to='apps_api.CDriveApplication')),
                ('cdrive_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filepermission_file', to='drive_api.CDriveFile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filepermission_user', to='user_mgmt.CDriveUser')),
            ],
        ),
        migrations.AddField(
            model_name='cdrivefile',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cdrivefile_parent', to='drive_api.CDriveFolder'),
        ),
        migrations.AddConstraint(
            model_name='cdrivefolder',
            constraint=models.UniqueConstraint(fields=('name', 'parent'), name='unique_folder'),
        ),
        migrations.AddConstraint(
            model_name='cdrivefile',
            constraint=models.UniqueConstraint(fields=('name', 'parent'), name='unique_file'),
        ),
        migrations.RunPython(create_home),
    ]
