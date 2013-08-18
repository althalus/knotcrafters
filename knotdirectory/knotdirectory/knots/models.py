from django.db import models
from taggit.managers import TaggableManager


class Knot(models.Model):
    name = models.CharField(max_length=90, help_text="Commonly accepted name for this tie")
    other_names = models.TextField(help_text="Is this knot known by other names? One name per line, please")
    creator = models.CharField(max_length=90, help_text="Who should we credit for discovering this tie")
    notes = models.TextField(help_text="Any other information? Markdown text enabled.")
    tags = TaggableManager()
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to="knotsimages/%Y/%m/", help_text="A photo of the completed tie.", null=True, blank=True)


class Link(models.Model):
    knot = models.ForeignKey(Knot)
    link = models.URLField(help_text="Link ot the guide")
    name = models.CharField(max_length=90, help_text="A descriptive name for this guide")
