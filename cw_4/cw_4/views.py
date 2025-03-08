from django.shortcuts import render, get_object_or_404, redirect
from .models import Thread, Post
from .forms import ThreadForm, PostForm

def redirect_to_threads(request):
    return redirect("thread_list")

def thread_list(request):
    threads = Thread.objects.all()
    if request.method == "POST":
        form = ThreadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("thread_list")
    else:
        form = ThreadForm()
    return render(request, "post/thread_list.html", {"threads": threads, "form": form})

def thread_detail(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    posts = Post.objects.filter(thread=thread)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread
            post.save()
            return redirect("thread_detail", pk=thread.pk)
    else:
        form = PostForm()

    return render(request, "post/thread_detail.html", {"thread": thread, "posts": posts, "form": form})

def thread_edit(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    if request.method == "POST":
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            return redirect("thread_detail", pk=thread.pk)
    else:
        form = ThreadForm(instance=thread)
    return render(request, "post/thread_edit.html", {"form": form, "thread": thread})

def thread_delete(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    thread.delete()
    return redirect("thread_list")

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("thread_detail", pk=post.thread.pk)
    else:
        form = PostForm(instance=post)
    return render(request, "post/post_edit.html", {"form": form, "post": post})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    thread_pk = post.thread.pk
    post.delete()
    return redirect("thread_detail", pk=thread_pk)
