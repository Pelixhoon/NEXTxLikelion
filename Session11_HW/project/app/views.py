from django.shortcuts import render, redirect
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def list_page(request):
    posts = Post.objects.all()

    return render(request, 'app/list_page.html', {'posts': posts})

@login_required(login_url='/registration/login')
def new(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        new_post = Post.objects.create(
            title=title, content=content, author=request.user
        )
        return redirect('detail_page', new_post.pk)
    
    return render(request, 'app/create_page.html')

@login_required(login_url='/registration/login')
def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.hits += 1
    post.save()
    
    print(type(post.author), 'post.author')
    if request.method == 'POST':
        content = request.POST['content']
        Comment.objects.create(post=post, content=content, author=request.user)

        return redirect('detail_page', post_pk)
    return render(request, 'app/detail_page.html', {'post':post})


def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('detail_page', post_pk)


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

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        found_user = User.objects.filter(username=username)
        if len(found_user):
            error = '이미 아이디가 존재합니다'
            return render(request, 'registration/signup.html', {'error':error})
        new_user = User.objects.create_user(username=username, password=password)
        auth.login(request, new_user)
        return redirect('home')
    return render(request, 'registration/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(
                request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect(request.GET.get('next','/'))
        error = '아이디 또는 비밀번호가 틀립니다'
        return render(request, 'registration/login.html', {'error': error})
    return render(request, 'registration/login.html')

def logout(request):
    auth.logout(request)

    return redirect('home')




 