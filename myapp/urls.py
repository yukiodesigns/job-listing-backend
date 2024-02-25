
from django.urls import path
from .views import UserCreateAPIView, CustomAuthToken
from .views_api import JobListCreateAPIView, JobRetrieveUpdateDestroyAPIView,ApplicationListCreateAPIView,ApplicationRetrieveUpdateDestroyAPIView, CompanyListCreateAPIView, CompanyRetrieveUpdateDestroyAPIView, UserRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('users/', UserCreateAPIView.as_view(), name='user-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),
    # path('auth/token/', CustomAuthToken.as_view(), name='get-token'),
    path('jobs/', JobListCreateAPIView.as_view(), name='job-list-create'),
    path('jobs/<int:pk>/', JobRetrieveUpdateDestroyAPIView.as_view(), name='job-retrieve-update-destroy'),
    path('applications/', ApplicationListCreateAPIView.as_view(), name='application-list-create'),
    path('applications/<int:pk>/', ApplicationRetrieveUpdateDestroyAPIView.as_view(), name='application-retrieve-update-destroy'),
    path('companies/', CompanyListCreateAPIView.as_view(), name='company-list-create'),
    path('companies/<int:pk>/', CompanyRetrieveUpdateDestroyAPIView.as_view(), name='company-retrieve-update-destroy'),
]


