# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from account.models import User


class DateMixin(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
            abstract = True

class Category(DateMixin):
    """Category model"""

    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):         
            return self.name


class Video(DateMixin):
    """Video model"""

    uploader = models.ForeignKey(User, null=True, blank=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, null=True, blank=True)
    views = models.PositiveIntegerField(null=True, blank=True, default=0)
    file = models.FileField(upload_to='videos/', null=True, blank=True)
    thumbnail = models.ImageField(
        upload_to='thumbnails/',
        max_length=500,
        null=True,
        blank=True
    )

    def __str__(self):
		return u'%s - %s' % (self.title, self.uploader)

class Comment(DateMixin):
	 """Video model"""

	 author = models.ForeignKey(User, null=True, blank=True)
	 content = models.TextField(blank=True, null=True)
	 video = models.ForeignKey(Video, null=True, blank=True)

	 def __str__(self):
		return u'%s - %s' % (self.author, self.video)

class Like(DateMixin):
	 """Like model"""

	 author = models.ForeignKey(User, null=True, blank=True)
	 video = models.ForeignKey(Video, null=True, blank=True)

	 def __str__(self):
		return u'%s - %s' % (self.author, self.video)

class Dislike(DateMixin):
	 """Dislike model"""

	 author = models.ForeignKey(User, null=True, blank=True)
	 video = models.ForeignKey(Video, null=True, blank=True)

	 def __str__(self):
	 	return u'%s - %s' % (self.author, self.video)
