from django.urls import path
from .views import (
    CatalogoFarmaciaListView,
    CatalogoFarmaciaCreateView,
    CatalogoFarmaciaUpdateView,
    CatalogoFarmaciaDeleteView,
)

urlpatterns = [
    path('', CatalogoFarmaciaListView.as_view(), name='catalogo_list'),
    path('crear/', CatalogoFarmaciaCreateView.as_view(), name='catalogo_create'),
    path('editar/<int:pk>/', CatalogoFarmaciaUpdateView.as_view(), name='catalogo_update'),
    path('eliminar/<int:pk>/', CatalogoFarmaciaDeleteView.as_view(), name='catalogo_delete'),
]
