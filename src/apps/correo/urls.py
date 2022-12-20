from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.CreateEmailServiceView.as_view(), name='create_email_service'),
]