# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Job'
        db.create_table(u'jobs_job', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True)),
            ('structure', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('topology', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('iterations', self.gf('django.db.models.fields.IntegerField')(default=10)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='jobs', to=orm['auth.User'])),
            ('status', self.gf('django.db.models.fields.CharField')(default='New', max_length=100, blank=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'jobs', ['Job'])

        # Adding model 'Result'
        db.create_table(u'jobs_result', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('job', self.gf('django.db.models.fields.related.ForeignKey')(related_name='result', to=orm['jobs.Job'])),
            ('gb', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('non_polar', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('reaction_field', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('solvent_intershell', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('solvent_intrashell', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('solvent_solute', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('total', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('sasa', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('shell_zero_waters', self.gf('django.db.models.fields.FloatField')(default=0.0)),
        ))
        db.send_create_signal(u'jobs', ['Result'])


    def backwards(self, orm):
        # Deleting model 'Job'
        db.delete_table(u'jobs_job')

        # Deleting model 'Result'
        db.delete_table(u'jobs_result')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'jobs.job': {
            'Meta': {'ordering': "('created_on',)", 'object_name': 'Job'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iterations': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'jobs'", 'to': u"orm['auth.User']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'New'", 'max_length': '100', 'blank': 'True'}),
            'structure': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'topology': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'jobs.result': {
            'Meta': {'object_name': 'Result'},
            'gb': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'result'", 'to': u"orm['jobs.Job']"}),
            'non_polar': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'reaction_field': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'sasa': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'shell_zero_waters': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'solvent_intershell': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'solvent_intrashell': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'solvent_solute': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'total': ('django.db.models.fields.FloatField', [], {'default': '0.0'})
        }
    }

    complete_apps = ['jobs']