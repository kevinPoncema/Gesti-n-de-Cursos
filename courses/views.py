from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from courses.serializers import AuthSerializer
from courses.services import AuthService
from courses.repository import UserRepository

class RegisterView(APIView):
    def post(self, request):
        serializer = AuthSerializer(data=request.data)
        if serializer.is_valid():
            user_repository = UserRepository()
            auth_service = AuthService(user_repository)
            try:
                user = auth_service.register_user(serializer.validated_data, request)
                return Response({
                    "message": "Usuario registrado exitosamente",
                    "user": {
                        "username": user.username,
                        "email": user.email,
                        "role": user.role
                    }
                }, status=status.HTTP_201_CREATED)
            except PermissionError as e:
                return Response({"error": str(e)}, status=status.HTTP_403_FORBIDDEN)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterStudentView(APIView):
    def post(self, request):
        serializer = AuthSerializer(data=request.data)
        # Remove role because students should always have 'student' role
        if 'role' in serializer.initial_data:
            serializer.initial_data.pop('role')
            
        if serializer.is_valid():
            user_repository = UserRepository()
            auth_service = AuthService(user_repository)
            user = auth_service.register_student(serializer.validated_data)
            return Response({
                "message": "Estudiante registrado exitosamente",
                "user": {
                    "username": user.username,
                    "email": user.email,
                    "role": user.role
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)