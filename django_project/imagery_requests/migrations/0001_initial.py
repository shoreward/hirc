# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CustomUser'
        db.create_table(u'imagery_requests_customuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'imagery_requests', ['CustomUser'])

        # Adding M2M table for field groups on 'CustomUser'
        m2m_table_name = db.shorten_name(u'imagery_requests_customuser_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('customuser', models.ForeignKey(orm[u'imagery_requests.customuser'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['customuser_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'CustomUser'
        m2m_table_name = db.shorten_name(u'imagery_requests_customuser_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('customuser', models.ForeignKey(orm[u'imagery_requests.customuser'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['customuser_id', 'permission_id'])

        # Adding model 'RequestStatus'
        db.create_table(u'imagery_requests_requeststatus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal(u'imagery_requests', ['RequestStatus'])

        # Adding model 'RequestDate'
        db.create_table(u'imagery_requests_requestdate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('time', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('imagery_request', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['imagery_requests.ImageryRequest'])),
        ))
        db.send_create_signal(u'imagery_requests', ['RequestDate'])

        # Adding model 'QuestionSet'
        db.create_table(u'questions_questionset', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'questions', ['QuestionSet'])

        # Adding M2M table for field questions on 'QuestionSet'
        m2m_table_name = db.shorten_name(u'questions_questionset_questions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('questionset', models.ForeignKey(orm[u'questions.questionset'], null=False)),
            ('question', models.ForeignKey(orm[u'questions.question'], null=False))
        ))
        db.create_unique(m2m_table_name, ['questionset_id', 'question_id'])

        # Adding model 'Question'
        db.create_table(u'questions_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'questions', ['Question'])

        # Adding model 'ImageryRequest'
        db.create_table(u'imagery_requests_imageryrequest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='created', to=orm['imagery_requests.CustomUser'])),
            ('area_of_interest', self.gf('django.contrib.gis.db.models.fields.PolygonField')()),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['imagery_requests.RequestStatus'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('request_lead', self.gf('django.db.models.fields.related.ForeignKey')(related_name='request_lead', null=True, to=orm['imagery_requests.CustomUser'])),
            ('question_set', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['questions.QuestionSet'], null=True)),
        ))
        db.send_create_signal(u'imagery_requests', ['ImageryRequest'])

        # Adding model 'Answer'
        db.create_table(u'questions_answer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['questions.Question'])),
            ('imagery_request', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['imagery_requests.ImageryRequest'])),
        ))
        db.send_create_signal(u'questions', ['Answer'])

    def backwards(self, orm):
        # Deleting model 'CustomUser'
        db.delete_table(u'imagery_requests_customuser')

        # Removing M2M table for field groups on 'CustomUser'
        db.delete_table(db.shorten_name(u'imagery_requests_customuser_groups'))

        # Removing M2M table for field user_permissions on 'CustomUser'
        db.delete_table(db.shorten_name(u'imagery_requests_customuser_user_permissions'))

        # Deleting model 'RequestStatus'
        db.delete_table(u'imagery_requests_requeststatus')

        # Deleting model 'RequestDate'
        db.delete_table(u'imagery_requests_requestdate')

        # Deleting model 'ImageryRequest'
        db.delete_table(u'imagery_requests_imageryrequest')

        # Deleting model 'QuestionSet'
        db.delete_table(u'questions_questionset')

        # Removing M2M table for field questions on 'QuestionSet'
        db.delete_table(db.shorten_name(u'questions_questionset_questions'))

        # Deleting model 'Question'
        db.delete_table(u'questions_question')

        # Deleting model 'Answer'
        db.delete_table(u'questions_answer')


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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'imagery_requests.customuser': {
            'Meta': {'object_name': 'CustomUser'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'imagery_requests.imageryrequest': {
            'Meta': {'object_name': 'ImageryRequest'},
            'area_of_interest': ('django.contrib.gis.db.models.fields.PolygonField', [], {}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'created'", 'to': u"orm['imagery_requests.CustomUser']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question_set': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['questions.QuestionSet']", 'null': 'True'}),
            'request_lead': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'request_lead'", 'null': 'True', 'to': u"orm['imagery_requests.CustomUser']"}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['imagery_requests.RequestStatus']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'imagery_requests.requestdate': {
            'Meta': {'object_name': 'RequestDate'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagery_request': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['imagery_requests.ImageryRequest']"}),
            'time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'imagery_requests.requeststatus': {
            'Meta': {'object_name': 'RequestStatus'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'questions.question': {
            'Meta': {'object_name': 'Question'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'questions.questionset': {
            'Meta': {'object_name': 'QuestionSet'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'questions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['questions.Question']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'questions.answer': {
            'Meta': {'object_name': 'Answer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagery_request': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['imagery_requests.ImageryRequest']"}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['questions.Question']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['imagery_requests']