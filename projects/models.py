import os

from django.db import models
from django.conf import settings

# Create your models here.

IMG_REL_PATH = "projects/img"


def get_img_abs_path():
    return os.path.join(settings.BASE_DIR, "projects/static", IMG_REL_PATH)


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path=get_img_abs_path)

    def __repr__(self):
        return self.title
