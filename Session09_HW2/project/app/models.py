from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50, default='')
    content = models.TextField(default='')
    hits = models.PositiveIntegerField(default=0, verbose_name='조회수')