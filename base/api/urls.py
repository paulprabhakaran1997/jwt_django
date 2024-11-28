from django.urls import path
from base.api import views

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path("",views.getRoutes),
    path('notes/',views.getNotes, name='get_notes'),

    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]