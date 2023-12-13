from django.urls import path
from .views import CustomAuthToken, register_user, api_1, api_2, api_3, api_4, crud_operations

urlpatterns = [
    path('api/login/', CustomAuthToken.as_view(), name='login'),
    path('api/register/', register_user, name='register'),
    path('api/api-1/', api_1, name='api_1'),   # Add more URL patterns for other views
    path('api/api-2/', api_2, name='api_2'),
    path('api/api-3/', api_3, name='api_3'),
    path('api/api-4/', api_4, name='api_4'),
    path('api/crud-operations/', crud_operations, name='crud_operations'),
    # Add more URL patterns for additional views as needed
    path('api/additional-view-1/', additional_view1, name='additional_view_1'),
    path('api/additional-view-2/', additional_view2, name='additional_view_2'),
    # Add more URL patterns for any other additional views as needed
]
