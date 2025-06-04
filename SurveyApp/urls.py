from django.urls import path, re_path
from django.urls import path
from .views import *

urlpatterns = [
    path('api/create-department',create_department),
    path('api/update-department/<id>/',update_department),
    path('api/get-all-epartment/',get_departments),
    path('api/delete-department/<id>/',delete_department),
]