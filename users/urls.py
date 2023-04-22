from django.urls import path
from .views import RegisterAPIView, LoginAPIView, UserDetailAPIView,LogoutAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('profile/', UserDetailAPIView.as_view(), name='profile'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
]
