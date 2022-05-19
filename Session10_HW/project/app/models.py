from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50, default='')
    content = models.TextField(default='')
    hits = models.PositiveIntegerField(default=0, verbose_name='조회수')

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()

    def __str__(self):
        return self.content