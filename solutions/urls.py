from django.urls import path, include
from .views import SolutionList, SolutionDetail, SolutionCreateAPI

urlpatterns = [
    path("list/", SolutionList.as_view()),
    path("<int:pk>/", SolutionDetail.as_view()),
    path("", SolutionCreateAPI.as_view())
]
