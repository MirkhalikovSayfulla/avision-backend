from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import (
    redirect,
    render,
    get_object_or_404
)

from blog.models import (
    Advertising,
    BlogNews,
    BlogVideo,
    Subscribe,
    Tag,
    Comment
)
from blog.weather import get_weather

temp, icon = get_weather("ташкент")

tags = Tag.objects.all()
advertising = Advertising.objects.last()
all_post = BlogNews.objects.all()
recent_videos = BlogVideo.objects.all().order_by("-id")[:5]
top_stories = BlogNews.objects.order_by('-id')[:5]
future_events = all_post.filter(events='Yes')


def home(request):
    blog_news_basic = all_post.filter(
        status='blog', category='Lifestyle')
    blog_news_external = all_post.filter(
        status='blog', category='Gadgets')
    home_news = all_post.filter(status='home').order_by('-id')[:2]
    dm_tags = Tag.objects.filter(category='dm')
    wt_tags = Tag.objects.filter(category='wt')

    context = {
        'pageName': 'Home',
        'home_news': home_news,
        'blog_news_basic_dm': blog_news_basic.filter(position='dm').order_by('-id')[:5],
        'blog_news_external_dm': blog_news_external.filter(position='dm').order_by('-id')[:10],
        'blog_news_basic_wt': blog_news_basic.filter(position='wt').order_by('-id')[:5],
        'blog_news_external_wt': blog_news_external.filter(position='wt').order_by('-id')[:10],
        'dm_tags': dm_tags,
        'wt_tags': wt_tags,
        'recent_posts': all_post.order_by('-id'),
        'trend_post': all_post.filter(position='wt').order_by('name')[:2],
        'advertising': advertising,
        'recent_videos': recent_videos,
        'future_events': all_post.filter(events='Yes').order_by('-id'),
        'top_stories': top_stories,
        'temperature': temp,
        'icon': icon,
        'title': 'Home'
    }
    return render(request, 'index.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        send_mail(f"Contact: {name}",
                  f"Name: {name}\nEmail: {email}\nMessage:\n{message}",
                  settings.EMAIL_HOST_USER,
                  ['mirxoliqov.sayfulla@gmail.com'],
                  fail_silently=False)
    context = {
        'pageName': 'Contact',
        'temperature': temp,
        'icon': icon,
        'title': 'Contact'
    }
    return render(request, 'contact.html', context)


def post(request, pk, types):
    if types == "post":
        item = get_object_or_404(BlogNews, id=pk)
    else:
        item = get_object_or_404(BlogVideo, id=pk)
        item.view = item.view + 1
        item.save()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        c = Comment(
            name=name,
            email=email,
            message=message,
            content_object=item,
        )
        c.save()

    context = {
        'pageName': 'Post',
        'title': item.name,
        'item': item,
        'temperature': temp,
        'icon': icon,
        'types': types,
        'recent_posts': all_post.order_by('-id')[:3],
        'comments': item.comments.order_by('-id'),
        'advertising': advertising,
        'recent_videos': recent_videos,
        'future_events': all_post.filter(events='Yes').order_by('-id'),
        'top_stories': top_stories,
    }
    return render(request, 'post.html', context)


def category_filter(request, category_name):
    if category_name == "Video":
        second_list = BlogVideo.objects.order_by('-id')
        object_list = False
    else:
        object_list = BlogNews.objects.filter(
            category=category_name
        ).order_by('-id')
        second_list = False

    context = {
        'pageName': "Category",
        'object_list': object_list,
        'tags': tags,
        'title': category_name,
        'temperature': temp,
        'icon': icon,
        'second_list': second_list,
        'advertising': advertising,
        'recent_videos': recent_videos,
        'future_events': all_post.filter(events='Yes').order_by('-id'),
        'top_stories': top_stories,
    }
    return render(request, 'category.html', context)


def filter_tag(request, tag_id):
    object_list = BlogNews.objects.filter(tag=tag_id)
    second_list = BlogVideo.objects.filter(tag=tag_id)
    context = {
        'pageName': "Category",
        'object_list': object_list,
        'tags': tags,
        'title': 'Tag',
        'temperature': temp,
        'icon': icon,
        'second_list': second_list,
        'advertising': advertising,
        'recent_videos': recent_videos,
        'future_events': all_post.filter(events='Yes').order_by('-id'),
        'top_stories': top_stories,
    }
    return render(request, 'category.html', context)


def search_result(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        blog_new = BlogNews.objects.filter(
            Q(name__contains=query)
        )
        blog_video = BlogVideo.objects.filter(
            Q(name__contains=query)
        )
        object_list = blog_new
        second_list = blog_video

    context = {
        'pageName': "Category",
        'temperature': temp,
        'object_list': object_list,
        'icon': icon,
        'title': query,
        'tags': tags,
        'second_list': second_list,
        'advertising': advertising,
        'recent_videos': recent_videos,
        'future_events': all_post.filter(events='Yes').order_by('-id'),
        'top_stories': top_stories,
    }
    return render(request, 'category.html', context)


def addSubscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        Subscribe.objects.create(
            email=email
        )
    return redirect('home')
