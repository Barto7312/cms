from django.shortcuts import render
from .models import Post

# Create your views here.

def post_list(request):
    post = Post.objects.filter(status='published')
    template = 'blog/post/post_list.html'
    context = {'post': post}
    return render(request, template, context)


