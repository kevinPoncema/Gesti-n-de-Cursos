from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from courses.serializers import RegisterSerializer
from courses.services import AuthService

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            auth_service = AuthService()
            try:
                user = list(auth_service.register_user(serializer.validated_data, request).values())
                return Response({"message": "Usuario registrado exitosamente"}, 
                                status=status.HTTP_201_CREATED
                                ,user=user)
            except PermissionError as e:
                return Response({"error": str(e)}, status=status.HTTP_403_FORBIDDEN)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)