from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Post, Category, Comment
from .forms import CommentForm

# Create your views here.


class BlogIndex(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    ordering = ["-created_on"]


class BlogCategoryIndex(generic.ListView):
    model = Post
    template_name = "blog/index.html"

    def get_queryset(self):
        return Post.objects.filter(categories__name=self.kwargs['category']).order_by("-created_on")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.kwargs['category']
        return context


class BlogDetail(generic.DetailView):
    model = Post
    template_name = "blog/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        comments = Comment.objects.filter(post=self.get_object()).order_by("-created_on")
        context['comments'] = comments
        context['form'] = CommentForm

        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
            return HttpResponseRedirect(reverse("blog:detail", args=(post.pk,)))
        return render(request, reverse("blog:detail", args=(post.pk,)), {"form": form})
