from django.db import models

class BlogPost(models.Model):
    post_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    author_name = models.CharField(max_length=100)

class Comment(models.Model):
    post = models.ForeignKey(BlogPost)
    comment_text = models.CharField(max_length=10000)
    pub_date = models.DateTimeField()
    author_name = models.CharField(max_length=200)

