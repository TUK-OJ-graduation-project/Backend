from django.urls import path
from .views import ProblemListAPI, ProblemAPI, ProblemCreateAPI, ProblemsByTypeAPI, ProblemsByLanguageAPI

urlpatterns = [
    path('list/', ProblemListAPI.as_view(), name='problem_list'),
    path('', ProblemCreateAPI.as_view(), name='problem_create'),
    path('<str:type>/<int:id>/', ProblemAPI.as_view(), name='problem_detail'),
    path('type/<str:type>/', ProblemsByTypeAPI.as_view(), name='problems_by_type'),
    path('language/<str:language>/', ProblemsByLanguageAPI.as_view(), name='problems_by_language'),
    # path('level/<int:level>/', ProblemsByLevelAPI.as_view(), name='problems_by_level'),
]

