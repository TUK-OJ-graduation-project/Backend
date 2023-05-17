from django.urls import path
from .views import SolutionCreateAPI

urlpatterns = [
    path('submit/', SolutionCreateAPI.as_view(), name='submit_solution'),
    path('submit/<int:pk>/', SolutionCreateAPI.as_view()),
]
