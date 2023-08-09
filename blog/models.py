from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# blog post status
STATUS = (
    (0, "Draft"),
    (1, "Publish"),
)

# the author model


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = CloudinaryField("image", default="placeholder")

    def __str__(self):
        return self.user.username


# model for posts
class Post(models.Model):
    title = models.CharField(max_length=25, unique=True)
    slug = models.SlugField(max_length=25, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    featured_image = CloudinaryField("image", default="placeholder")
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name="blog_likes", blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


# model for commenting on posts
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


# model for post categories

class Category(models.Model):
    CATEGORY_CHOICES = (
        ("1", "paintings"),
        ("2", "models and sculptures"),
        ("3", "street art"),
        ("4", "other"),
    )

    title = models.CharField(max_length=25)
    subtitle = models.CharField(max_length=25)
    slug = models.SlugField()
    thumbnail = CloudinaryField("image", default="placeholder")
    choices = CATEGORY_CHOICES

    def __str__(self):
        return self.title
