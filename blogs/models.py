# Create your models here.

from django.db import models
from django.core.urlresolvers import reverse

from ckeditor.fields import RichTextField
from tagging.fields import TagField

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return reverse ('category_view', kwargs={'slug': self.slug})


    def __unicode__(self):
        return self.name




class Blogs(models.Model):
    page_title = models.CharField(max_length=150, unique=True, verbose_name='Page Title', blank=True)
    title = models.CharField(max_length=150, unique=True, verbose_name='Title')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='URL')
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    meta_description = models.CharField(max_length=500, verbose_name='Meta Description', blank=True)
    meta_keywords = models.CharField(max_length=250, verbose_name='Meta Keywords', blank=True)
    body = RichTextField()
    category = models.ForeignKey(Categories)
    publish = models.BooleanField(default=None)
    tags = TagField()

    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Blogs"


    def get_absolute_url(self):
        return reverse ('blog_view', kwargs={'slug': self.slug})


    def __unicode__(self):
        return self.title









