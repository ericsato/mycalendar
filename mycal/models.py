from django.db import models
from django.db.models import permalink
import datetime

# Create your models here.
class Date(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    date = models.DateField()
    type = models.ForeignKey('mycal.Type')
    relationship = models.ForeignKey('mycal.Relationship')


    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_mycal_date', None, { 'slug': self.slug })

    def get_day(self):
        return self.date.strftime('%d')

    def get_year(self):
        return self.date.strftime('%Y')

    def get_duration(self):
        return (int(datetime.datetime.now().year) - int(self.date.year))

class Type(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_mycal_type', None, { 'slug': self.slug })


class Relationship(models.Model):
    relationship = models.CharField(max_length=100, default="friend")
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.relationship

    @permalink
    def get_absolute_url(self):
        return ('view_mycal_relationship', None, { 'slug': self.slug })

