# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import *
from django.contrib.auth.models import *
from django.contrib import admin

# Create your models here.
class EyeTrackerSession(models.Model):
    password = models.CharField(max_length=100, blank=False)
    username = models.CharField(max_length=100, blank=False)
    cybertrustpath = models.CharField(max_length=1000, blank=False)
