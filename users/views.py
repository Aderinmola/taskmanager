from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterUserSerializer, ProfileSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from drf_yasg.utils import swagger_auto_schema


class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=RegisterUserSerializer)
    def post(self, request):
        reg_serializer = RegisterUserSerializer(data=request.data)
        if reg_serializer.is_valid():
            newuser = reg_serializer.save()
            if newuser:
                return Response(
                    {"message": "User created successfully!!!"},
                    status=status.HTTP_201_CREATED, 
                    )
            return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class GetCurrentUser(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile_serializer = ProfileSerializer(request.user)        
        return Response(
            # {"message": "User created successfully!!!"},
            profile_serializer.data,
            status=status.HTTP_200_OK, 
            )
