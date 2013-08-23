from django.db import models
from taggit.managers import TaggableManager
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.auth import get_user_model


User = get_user_model()


class Knot(models.Model):
    name = models.CharField(max_length=90, help_text="Commonly accepted name for this tie")
    other_names = models.TextField(help_text="Is this knot known by other names? One name per line, please", blank=True)
    creator = models.CharField(max_length=90, help_text="Who should we credit for discovering this tie")
    notes = models.TextField(help_text="Any other information? Markdown text enabled.", blank=True)
    tags = TaggableManager()
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to="knotsimages/%Y/%m/", help_text="A photo of the completed tie.", null=True, blank=True)

    def get_absolute_url(self):
        return reverse("knots.detail", args=[self.pk, ])

    def __unicode__(self):
        return u'%s' % self.name


class Link(models.Model):
    knot = models.ForeignKey(Knot)
    link = models.URLField(help_text="Link ot the guide")
    name = models.CharField(max_length=90, help_text="A descriptive name for this guide")

    def __unicode__(self):
        return u'Link %s on knot %s' % (self.name, self.knot.name)


class Action(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    user = models.ForeignKey(User)
    when = models.DateTimeField(auto_now=True)
    what = models.TextField()

    def __unicode__(self):
        return u'%s: %s %s %s' % (self.when, self.user, self.what, self.content_object)


class CreatorProfile(models.Model):
    name = models.CharField(max_length=90)
    link_facebook_profile = models.URLField(blank=True)
    link_youtube_channel = models.URLField(blank=True)
    link_website = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    user = models.ForeignKey(User, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.name
