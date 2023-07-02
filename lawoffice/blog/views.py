from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic import ListView, View
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound
from django.utils.html import format_html

from .models import Post
from .forms import CommentForm

import re
# Create your views here.


class BlogHomePage(ListView):
    model = Post
    template_name = 'blog/blog-main-page.html'
    ordering = ['-id']
    context_object_name = 'posts'


class SinglePost(View):

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        post.content = self.add_hard_space(post.content)

        context = {
            "post": post,
            "post_tags": post.tag.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("id"),

        }
        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            return HttpResponseRedirect(reverse("post-detail", args=[slug]))

        context = {
            "post": post,
            "post_tags": post.tag.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id"),
            "saved_for_lat": self.is_stored_post(request, post.id)
        }
        return render(request, "blog/post-detail.html", context)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_tags'] = self.objects.tag.all()
        context['comment_form'] = CommentForm()
        return context



    def add_hard_space(self, text):
        regex = r"\b([a-zA-Z]{1,3})\s?\b"
        new_text = re.sub(regex, r'\1&nbsp;', text)
        return new_text

    # def post_detail(self, request, post_id):
    #     post = Post.objects.get(pk=post_id)
    #     post.content = self.add_hard_space(post.content)
    #     return render(request, 'post_detail.html', {'post': post})