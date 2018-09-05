# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Expense(models.Model):
    text=models.CharField(max_length=255)
    date=models.DateTimeField('DAte')
    amount=models.BigIntegerField()
    user=models.ForeignKey(User)
    def __unicode__(self):
        return "{}-{}".format(self.date,self.amount)

class Income (models.Model): # mige az models ye chizi daram ke Model hastesh
    text=models.CharField(max_length=255)
    date= models.DateTimeField('Date')
    amount=models.BigIntegerField()
    user=models.ForeignKey(User)
    def __unicode__(self):
        return "{}-{}".format(self.date,self.amount)
