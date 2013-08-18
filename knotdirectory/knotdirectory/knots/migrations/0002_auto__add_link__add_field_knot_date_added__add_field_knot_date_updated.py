# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Link'
        db.create_table(u'knots_link', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('knot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['knots.Knot'])),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=90)),
        ))
        db.send_create_signal(u'knots', ['Link'])

        # Adding field 'Knot.date_added'
        db.add_column(u'knots_knot', 'date_added',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 8, 18, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Knot.date_updated'
        db.add_column(u'knots_knot', 'date_updated',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 8, 18, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Knot.photo'
        db.add_column(u'knots_knot', 'photo',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Link'
        db.delete_table(u'knots_link')

        # Deleting field 'Knot.date_added'
        db.delete_column(u'knots_knot', 'date_added')

        # Deleting field 'Knot.date_updated'
        db.delete_column(u'knots_knot', 'date_updated')

        # Deleting field 'Knot.photo'
        db.delete_column(u'knots_knot', 'photo')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'knots.knot': {
            'Meta': {'object_name': 'Knot'},
            'creator': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'other_names': ('django.db.models.fields.TextField', [], {}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'knots.link': {
            'Meta': {'object_name': 'Link'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'knot': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['knots.Knot']"}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '90'})
        },
        u'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'taggit.taggeditem': {
            'Meta': {'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_tagged_items'", 'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_items'", 'to': u"orm['taggit.Tag']"})
        }
    }

    complete_apps = ['knots']