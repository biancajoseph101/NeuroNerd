from django.db import models
from django.conf import settings

# Create your models here.


class Tag(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.TextField()

    def __str__(self):
        return self.category_name


class Post(models.Model):
    category = models.ForeignKey(
        Tag, related_name="tag_list", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100, default='no post title')
    date = models.DateField(blank=True, auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="posts", on_delete=models.CASCADE)
    content = models.TextField()
    image_url = models.TextField()
    source = models.TextField()

    def __str__(self):
        return self.title


class ResourceType(models.Model):
    resource_type = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    picture = models.TextField(blank=True)

    def __str__(self):
        return self.resource_type


class Resource(models.Model):
    resource_type = models.ManyToManyField(
        ResourceType, related_name="resource_list", blank=True
    )
    topic = models.CharField(max_length=100)
    link = models.URLField(blank=True)
    image = models.TextField(blank=True)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.topic
