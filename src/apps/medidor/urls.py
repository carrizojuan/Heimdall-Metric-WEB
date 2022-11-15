from django.urls import path
import apps.medidor.views as views

app_name = 'medidor'

urlpatterns = [
    path("crear", views.CrearMedidorView.as_view(), name="crear_medidor"),
    path("listar", views.ListMedidoresView.as_view(), name="listar_medidores")
]