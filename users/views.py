from rest_framework.views import APIView
from .serializers import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser

# 회원가입 뷰
class RegisterAPIView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Access the JWT token
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user": serializer.data,
                    "message": "가입 성공",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_201_CREATED,
            )

            # JWT token => store in cookie
            res.set_cookie("access", access_token, httponly=True)
            res.set_cookie("refresh", refresh_token, httponly=True)

            return res
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 로그인 뷰
class LoginAPIView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

# 로그아웃 뷰   
class LogoutAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request): # delete 함수 써도 되지만 클라이언트 입장에선 요청보낼때 post가 편하다구함.
        response = Response({"message": "로그아웃 성공"}, status=status.HTTP_200_OK)
        response.delete_cookie("access")
        response.delete_cookie("refresh")
        return response

# 회원정보 보기/수정 
class UserDetailAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        serializer = CustomUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request):
        user = request.user
        serializer = CustomUserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)