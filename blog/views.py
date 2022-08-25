from time import timezone
from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.

def post_list(req):
    # get only the posts that are published and order them by the published date
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(req, 'blog/post_list.html', {'posts': posts})