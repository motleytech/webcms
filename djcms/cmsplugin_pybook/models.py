from django.db import models
from cms.models.pluginmodel import CMSPlugin

# Create your models here.

class PyBookName(CMSPlugin):
    pybookName = models.CharField(max_length=250, default='-- name of pybook --')

