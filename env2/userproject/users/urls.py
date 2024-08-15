from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),

    path('worker/', WorkerView.as_view(), name='WorkerView'),
    path('worker/<int:pk>/', WorkerDetail.as_view(), name='WorkerDetail'),
]