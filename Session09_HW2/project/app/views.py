from django.shortcuts import render, redirect
from .models import Post


def list_page(request):
    posts = Post.objects.all()

    return render(request, 'app/list_page.html', {'posts': posts})


def create_page(request):
    if request.method == 'POST':
        new_post = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content']
        )
        return redirect('detail_page', new_post.pk)
    return render(request, 'app/create_page.html')


def detail_page(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.hits += 1
    post.save()
    
    return render(request, 'app/detail_page.html', {"post": post})


def edit_page(request, post_pk):
    post = Post.objects.filter(pk=post_pk)
    if request.method == 'POST':
        post.update(
            title = request.POST['title'],
            content = request.POST['content']
        )
        return redirect('detail_page', post_pk)
    return render(request, 'app/edit_page.html', {'post':post[0]})


def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('list_page')
