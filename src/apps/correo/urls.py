from django.urls import path
from . import views

app_name = 'email_service'


urlpatterns = [
    path('crear/', views.CreateEmailServiceView.as_view(), name='create_email_service'),
    path('<int:pk>/delete/', views.email_service_delete, name='email_service_delete'),
    path('<int:pk>/', views.EmailServiceDetailView.as_view(), name='email_service_detail'),
    path('', views.EmailServiceListView.as_view(), name='email_service_list'),
]