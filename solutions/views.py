from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Solution
from .serializers import SolutionSerializer

class SolutionList(APIView):
    def get(self, request): # 전체 솔루션 목록 조회
        solutions = Solution.objects.all()
        serializer = SolutionSerializer(solutions, many=True)
        return Response(serializer.data)

class SolutionDetail(APIView):
    def get(self, request, pk): # 특정 문제에 대한 솔루션 조회
        solution = get_object_or_404(Solution, pk=pk)
        serializer = SolutionSerializer(solution)
        return Response(serializer.data)

    def put(self, request, pk): # 특정 문제애 대한 솔루션 전체수정
        solution = get_object_or_404(Solution, pk=pk)
        serializer = SolutionSerializer(solution, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk): # 특정 문제에 대한 솔루션 부분수정
        solution = get_object_or_404(Solution, pk=pk)
        serializer = SolutionSerializer(solution, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    ''' def delete(self, request, pk):
        solution = get_object_or_404(Solution, pk=pk)
        solution.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) '''

class SolutionCreateAPI(APIView):
    def post(self, request): # 문제에 대한 솔루션 작성 (생성)
        serializer = SolutionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
