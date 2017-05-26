# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import *
from django.contrib.auth.models import *
from django.contrib import admin

from picklefield.fields import PickledObjectField
# Create your models here.
class EyeTrackerSession(models.Model):
    args = PickledObjectField(default =[])

    def args_unpacked(self):
        return u'{args}'.format(args=self.args)

    class Admin(admin.ModelAdmin):
        list_display = ('id','args_unpacked',)
