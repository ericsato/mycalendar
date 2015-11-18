from django.db import models
from django.db.models import permalink

# Create your models here.
class Date(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    date = models.DateField()
    type = models.ForeignKey('mycalendar.Type')
    relationship = models.ForeignKey('mycalendar.Relationship')


    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_mycalendar_date', None, { 'slug': self.slug })

    def get_day(self):
        return self.date.strftime('%d')

class Type(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_mycalendar_type', None, { 'slug': self.slug })


class Relationship(models.Model):
    relationship = models.CharField(max_length=100, default="friend")
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.relationship

    @permalink
    def get_absolute_url(self):
        return ('view_mycalendar_relationship', None, { 'slug': self.slug })

