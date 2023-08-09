from django.shortcuts import render
from django.views import generic
from .models import Post, Category, Author


# homepage view
class homepage(request):
    categories = Category.objects.all()[0:3]
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by("-timestamp")[0:3]
    context = {
        "object_list": featured,
        "latest": latest,
        "categories": categories
    }

    return render(request, "index.html", context)
# view to see all posts
class all_posts(generic.ListView)
