from django.urls import path
from news import views




urlpatterns = [
    # path('', views.NewsList.as_view(), name='index'),
    path('', views.NewsTemplateView.as_view(), name='index'),
    path('category', views.category, name='category'),
    path('contact', views.contact, name='contact'),
    path('elements', views.elements, name='elements'),
    path('singlepost', views.singlepost, name='singlepost'),
    path('news/create', views.NewsCreateView.as_view(), name='create_news'),
    path('news/<str:category>/<int:pk>/',views.NewsDetailView.as_view(), name="detail_news"),
    path('news/<str:category>/<int:pk>/delete_news/',views.NewsDetailDelete.as_view(), name="delete_news"),
    path('news/<str:category>/<int:pk>/update_news/',views.NewsDetailEdit.as_view(), name="update_news"),
    path('news/<str:category>/<int:news_id>/comment/',views.comments, name="comment_news"),
    
]