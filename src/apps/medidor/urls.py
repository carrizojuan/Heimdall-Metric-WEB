from django.urls import path
import apps.medidor.views as views

app_name = 'medidor'

urlpatterns = [
    path("crear", views.CrearMedidorView.as_view(), name="crear_medidor"),
    path("listar", views.ListMedidoresView.as_view(), name="listar_medidores"),
    path("editar/<int:pk>", views.EditarMedidorView.as_view(), name="editar_medidor"),
    path("detalle/<int:pk>", views.MedidorDetalleView.as_view(), name="detalle_medidor"),
    path("eliminar/<int:pk>", views.eliminar_medidor, name="eliminar_medidor")
]