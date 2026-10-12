from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import CatalogoFarmaciaForm
from .models import CatalogoFarmacia


class CatalogoFarmaciaListView(ListView):
    model = CatalogoFarmacia
    template_name = "farmacia/catalogo_list.html"
    context_object_name = "productos"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        productos = list(context["productos"])
        context["stats"] = {
            "total": len(productos),
            "stock_total": sum(p.stock for p in productos),
            "valor_inventario": sum(p.precio * p.stock for p in productos),
            "por_vencer": sum(1 for p in productos if p.estado == "por_vencer"),
            "vencidos": sum(1 for p in productos if p.estado == "vencido"),
            "stock_max": max((p.stock for p in productos), default=0),
        }
        return context


class CatalogoFarmaciaCreateView(CreateView):
    model = CatalogoFarmacia
    form_class = CatalogoFarmaciaForm
    template_name = "farmacia/catalogo_form.html"
    success_url = reverse_lazy("catalogo_list")

    def form_valid(self, form):
        messages.success(self.request, "Producto creado exitosamente.")
        return super().form_valid(form)


class CatalogoFarmaciaUpdateView(UpdateView):
    model = CatalogoFarmacia
    form_class = CatalogoFarmaciaForm
    template_name = "farmacia/catalogo_form.html"
    success_url = reverse_lazy("catalogo_list")

    def form_valid(self, form):
        messages.success(self.request, "Producto actualizado correctamente.")
        return super().form_valid(form)


class CatalogoFarmaciaDeleteView(DeleteView):
    model = CatalogoFarmacia
    template_name = "farmacia/catalogo_confirm_delete.html"
    success_url = reverse_lazy("catalogo_list")

    def form_valid(self, form):
        messages.success(self.request, "Producto eliminado correctamente.")
        return super().form_valid(form)
