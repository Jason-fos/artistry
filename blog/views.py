from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post, Category, Author


# homepage view
class homepage(View):
    categories = Category.objects.all()[0:3]
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by("-timestamp")[0:3]
    template_name = "index.html"
    context = {
        "object_list": featured,
        "latest": latest,
        "categories": categories
    }


# view to see all posts
class all_posts(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "all_posts.html"
    paginate_by = 6
