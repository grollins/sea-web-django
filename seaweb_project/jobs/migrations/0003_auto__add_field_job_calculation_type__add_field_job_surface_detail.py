# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Job.calculation_type'
        db.add_column(u'jobs_job', 'calculation_type',
                      self.gf('django.db.models.fields.CharField')(default='dipole', max_length=20),
                      keep_default=False)

        # Adding field 'Job.surface_detail'
        db.add_column(u'jobs_job', 'surface_detail',
                      self.gf('django.db.models.fields.IntegerField')(default=8),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Job.calculation_type'
        db.delete_column(u'jobs_job', 'calculation_type')

        # Deleting field 'Job.surface_detail'
        db.delete_column(u'jobs_job', 'surface_detail')


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
            'Meta': {'ordering': "('created_on',)", 'unique_together': "(('owner', 'title'),)", 'object_name': 'Job'},
            'calculation_type': ('django.db.models.fields.CharField', [], {'default': "'dipole'", 'max_length': '20'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iterations': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'jobs'", 'to': u"orm['auth.User']"}),
            'status': ('model_utils.fields.StatusField', [], {'default': "'submitted'", 'max_length': '100', u'no_check_for_status': 'True'}),
            'status_changed': ('model_utils.fields.MonitorField', [], {'default': 'datetime.datetime.now', u'monitor': "u'status'"}),
            'structure': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'surface_detail': ('django.db.models.fields.IntegerField', [], {'default': '8'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'topology': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
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