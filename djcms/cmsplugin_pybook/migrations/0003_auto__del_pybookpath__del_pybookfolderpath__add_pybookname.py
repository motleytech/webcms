# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'PyBookPath'
        db.delete_table(u'cmsplugin_pybook_pybookpath')

        # Deleting model 'PyBookFolderPath'
        db.delete_table(u'cmsplugin_pybook_pybookfolderpath')

        # Adding model 'PyBookName'
        db.create_table(u'cmsplugin_pybook_pybookname', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('pybookName', self.gf('django.db.models.fields.CharField')(default='-- name of pybook --', max_length=250)),
        ))
        db.send_create_signal(u'cmsplugin_pybook', ['PyBookName'])


    def backwards(self, orm):
        # Adding model 'PyBookPath'
        db.create_table(u'cmsplugin_pybook_pybookpath', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('filePath', self.gf('django.db.models.fields.CharField')(default='-- full path to basic html file --', max_length=250)),
        ))
        db.send_create_signal(u'cmsplugin_pybook', ['PyBookPath'])

        # Adding model 'PyBookFolderPath'
        db.create_table(u'cmsplugin_pybook_pybookfolderpath', (
            ('folderPath', self.gf('django.db.models.fields.CharField')(default='-- full path to folder --', max_length=250)),
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'cmsplugin_pybook', ['PyBookFolderPath'])

        # Deleting model 'PyBookName'
        db.delete_table(u'cmsplugin_pybook_pybookname')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        u'cmsplugin_pybook.pybookname': {
            'Meta': {'object_name': 'PyBookName', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'pybookName': ('django.db.models.fields.CharField', [], {'default': "'-- name of pybook --'", 'max_length': '250'})
        }
    }

    complete_apps = ['cmsplugin_pybook']