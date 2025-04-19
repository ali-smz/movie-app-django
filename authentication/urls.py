from .views import CustomTokenObtainPairView , SignupView
from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('signup/', SignupView.as_view(), name='sign_up'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]