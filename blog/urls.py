from django.urls import path
from . views import PostView
from . import views

app_name = 'blog'  

urlpatterns = [
    path('blog/', views.PostView.as_view(), name='blog'),
    path('blog/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    
]