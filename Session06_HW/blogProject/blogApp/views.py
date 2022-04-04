from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def new(request):
    if request.method == 'POST':
        # POST 요청으로 온 데이터 확인
        print(request.POST)
        Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category']
        )
        return redirect('list')

    return render(request, 'new.html')

def list(request):
    hobbycount = len(Article.objects.filter(category='hobby'))
    foodcount = Article.objects.filter(category='food').count()
    programmingcount = len(Article.objects.filter(category='programming'))
    return render(request, 'list.html', {'hobbycount': hobbycount, 'foodcount': foodcount, 'programmingcount': programmingcount})

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'detail.html', {'article': article})

def category(request, category_name):
    articles = Article.objects.filter(category=category_name)
    return render(request, 'category.html', {'articles': articles})
