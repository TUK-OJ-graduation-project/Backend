import requests
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Solution
from .serializers import SolutionSerializer

class SolutionCreateAPI(APIView):
    def post(self, request):
        serializer = SolutionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            source_code = serializer.validated_data['source_code']
            res = requests.post('http://localhost:80/run', data={'script': source_code})
            
            try:
                result = res.json()
            except json.JSONDecodeError:
                return Response({'detail': f"Unexpected response from scoring server: {res.text}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            solution = Solution.objects.get(pk=serializer.data['id'])
            if "error" in result:
                solution.execution_result = result['error']
                solution.is_accepted = False
            else:
                output = result.get('output')
                solution.execution_result = output if output else 'The code was executed successfully!'
                solution.is_accepted = True
            solution.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        solution = get_object_or_404(Solution, pk=pk)
        serializer = SolutionSerializer(solution)
        return Response(serializer.data)
    
    def put(self, request, pk):
        solution = get_object_or_404(Solution, pk=pk)
        serializer = SolutionSerializer(solution, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)