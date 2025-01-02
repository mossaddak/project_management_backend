# Generated by Django 5.1.4 on 2025-01-02 12:39

import autoslug.fields
import commentio.helpers.slug_helpers
import dirtyfields.dirtyfields
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taskio', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=commentio.helpers.slug_helpers.get_task_comment_slug, unique=True)),
                ('status', models.CharField(choices=[('DRAFT', 'Draft'), ('PENDING', 'Pending'), ('PUBLISHED', 'Published'), ('REMOVED', 'Removed')], default='DRAFT', max_length=20)),
                ('kind', models.CharField(choices=[('TASK', 'Task'), ('PROJECT', 'Project')], max_length=20)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskio.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
    ]