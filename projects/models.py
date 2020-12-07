import os

from django.db import models
from django.conf import settings

# Create your models here.


def get_img_abs_path():
    return os.path.join(settings.BASE_DIR, "projects/static/projects/img")


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path=get_img_abs_path)

    def __repr__(self):
        return self.title
