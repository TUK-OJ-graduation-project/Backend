from django.urls import path, include
from .views import ProblemListAPI, ProblemAPI, ProblemCreateAPI

urlpatterns = [
    path("list/", ProblemListAPI.as_view()),
    path("<int:id>/", ProblemAPI.as_view()),
    path("", ProblemCreateAPI.as_view()),
]
