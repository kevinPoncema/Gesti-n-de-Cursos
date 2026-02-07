from django.urls import path
from . import views as courses_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    # JWT Tradicional (Login)
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Registro personalizado
    path('api/auth/register/', courses_views.RegisterView.as_view(), name='auth_register'),
]