from django.db import models

# Create your models here.


class Tag(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.TextField()

    def __str__(self):
        return self.category_name


class User(models.Model):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    is_logged_in = models.BooleanField()

    def __str__(self):
        return self.username


class Post(models.Model):
    category = models.ForeignKey(
        Tag, related_name="tag_list", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=50)
    date = models.DateField(blank=True, auto_now_add=True)
    author = models.ForeignKey(
        User, related_name="name", on_delete=models.CASCADE)
    # )
    # author = models.CharField(max_length=50)
    content = models.TextField()
    image_url = models.TextField()
    source = models.TextField()

    def __str__(self):
        return self.title
