from django.urls import path
from .views import QuestionView, AnswerView

urlpatterns = [
    path('questions/', QuestionView.as_view()), # 질문 리스트
    path('questions/<int:question_id>/', QuestionView.as_view()), # 질문 화면 보기
    path('answers/', AnswerView.as_view()), # 답변 리스트
    path('answers/<int:answer_id>/', AnswerView.as_view()), # 답변 화면 보기
]
