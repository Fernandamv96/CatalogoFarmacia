from django.urls import path

from .views import (
    CatalogoFarmaciaCreateView,
    CatalogoFarmaciaDeleteView,
    CatalogoFarmaciaListView,
    CatalogoFarmaciaUpdateView,
)

urlpatterns = [
    path("", CatalogoFarmaciaListView.as_view(), name="catalogo_list"),
    path("crear/", CatalogoFarmaciaCreateView.as_view(), name="catalogo_create"),
    path("editar/<int:pk>/", CatalogoFarmaciaUpdateView.as_view(), name="catalogo_update"),
    path("eliminar/<int:pk>/", CatalogoFarmaciaDeleteView.as_view(), name="catalogo_delete"),
]
