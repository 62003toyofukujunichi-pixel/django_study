from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)  # タイトル（最大100文字）
    content = models.TextField()               # 本文（長い文章）

    def __str__(self):
        return self.title