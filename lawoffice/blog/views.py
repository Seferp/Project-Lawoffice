from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic import ListView, View
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound

from .models import Post
from .forms import CommentForm

# Create your views here.


class BlogHomePage(ListView):
    model = Post
    template_name = 'blog/blog-main-page.html'
    ordering = ['-date']
    context_object_name = 'posts'


class SinglePost(View):

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)

        context = {
            "post": post,
            "post_tags": post.tag.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),

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
