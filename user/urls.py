from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from user.views.get_users_details import get_user_details

urlpatterns = [
    path('users/', get_user_details),
]

urlpatterns = format_suffix_patterns(urlpatterns)
