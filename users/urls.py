from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('registration/', views.UserRegistrationView.as_view(), name='registration'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('user-carts/', views.UserCartView.as_view(), name='user_carts'),
    path('logout/', views.logout, name='logout'),
]