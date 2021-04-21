# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    content = models.TextField(max_length=2048, null=True, blank=True)

    def __str__(self):
        return self.title
