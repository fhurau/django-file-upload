from django.urls import path
from .views import upload_profile
from .views import upload_profile, success

urlpatterns = [
    path('upload/', upload_profile, name='upload_profile'),
    path('success/', success, name='success'),
]
