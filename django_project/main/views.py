from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from .models import News
from .forms import UserRegistrationForm, CommentForm, NewsForm

def home(request):
    latest_news = News.objects.all().order_by('-pub_date')[:3]
    return render(request, 'main/home.html', {'latest_news': latest_news})

def news_list(request):
    news = News.objects.all().order_by('-pub_date')
    query = request.GET.get('q')
    
    if query:
        news = news.filter(title__icontains=query)
    
    return render(request, 'main/news_list.html', {
        'news_list': news,
        'query': query
    })

def news_detail(request, news_id):
    news = get_object_or_404(News, id=news_id)
    
    if request.method == 'POST' and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.news = news
            comment.author = request.user
            comment.save()
            return redirect('news_detail', news_id=news.id)
    else:
        comment_form = CommentForm()
    
    return render(request, 'main/news_detail.html', {
        'news': news,
        'comment_form': comment_form
    })

@login_required
def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()
            return redirect('news_detail', news_id=news.id)
    else:
        form = NewsForm()
    return render(request, 'main/news_form.html', {'form': form})

def contacts(request):
    return render(request, 'main/contacts.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация успешна!')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'main/register.html', {'form': form})