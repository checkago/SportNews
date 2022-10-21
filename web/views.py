from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from .forms import *
from django import views
from web.models import *


class IndexView(views.View):

    def get(self, request, *args, **kwargs):
        title = 'Новости бокса'
        description = 'Новости и события произошедшие в мировом боксе'
        news_list = Post.objects.all().order_by('-date')
        paginator = Paginator(news_list, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'index.html', {'title': title, 'news_list': news_list, 'paginator': paginator,
                                              'page_obj': page_obj, 'description': description})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    # List of active comments for this post
    comments = post.comments.filter(active=True)
    title = Post.name
    description = Post.description

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        comment_form = CommentForm()
    return render(request, 'news_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form,
                                                'title': title, 'description': description})

