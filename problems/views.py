from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.generics import CreateAPIView
from .models import Problem
from .serializers import ProblemSerializer

class ProblemListAPI(APIView):
    def get(self, request): # 전체 목록 가져오기
        problem_list = Problem.objects.all()
        serializer = ProblemSerializer(problem_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ProblemAPI(APIView): 
    def get(self, request, id): # 특정 문제 가져오기
        problem = get_object_or_404(Problem, id=id)
        serializer = ProblemSerializer(problem)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def delete(self, request, id): # 특정 문제 삭제
        problem = get_object_or_404(Problem, id=id)
        problem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

     
class ProblemCreateAPI(APIView):
    def post(self, request): # 문제 생성
        serializer = ProblemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
