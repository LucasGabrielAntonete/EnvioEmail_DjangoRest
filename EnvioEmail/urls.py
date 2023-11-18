from django.urls import path
from .views import EmailAPIView

urlpatterns = [
    path('email/', EmailAPIView.as_view(), name='email'),
]