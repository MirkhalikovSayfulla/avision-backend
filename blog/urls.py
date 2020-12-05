from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('post/<int:pk>/<str:types>/', views.post, name="post"),
    path('category/<str:category_name>/', views.category_filter, name="category"),
    path('tag/<int:tag_id>/', views.filter_tag, name='tag'),
    path('search/', views.search_result, name='search'),
    path('subscribe/', views.addSubscribe, name='subscribe'),
]
