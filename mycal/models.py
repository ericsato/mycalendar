from django.db import models
from django.db.models import permalink

# Create your models here.
class Date(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    type = models.ForeignKey('mycal.Type')

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_mycal_date', None, { 'slug': self.slug })

class Type(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_mycal_type', None, { 'slug': self.slug })