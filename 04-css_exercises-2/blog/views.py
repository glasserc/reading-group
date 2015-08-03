from django.shortcuts import render, get_object_or_404
from . import models

# Create your views here.
def list_posts(request):
    posts = models.BlogPost.objects.order_by('-pub_date')[:10]
    return render(request, "blog/index.html", {'posts': posts})


def show_post(request, post_id):
    post = get_object_or_404(models.BlogPost, pk=post_id)
    comments = post.comment_set.order_by('pub_date')
    return render(request, "blog/show_post.html", {
        'post': post, 'comments': comments
    })


def list_comments(request):
    comments = models.Comment.objects.order_by('-pub_date')[:10]
    return render(request, "blog/list_comments.html", {
        'comments': comments
    })


def show_comment(request, comment_id):
    comment = get_object_or_404(models.Comment, pk=comment_id)
    post = comment.post
    return render(request, "blog/show_comment.html", {
        'post': post, 'comment': comment
    })
