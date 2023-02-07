from django.urls import path, include
from .views import WorkList, RegisterAPI

urlpatterns = [
    path('api/works/', WorkList.as_view(), name='work-list'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
]