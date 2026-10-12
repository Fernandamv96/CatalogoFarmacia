from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .models import CatalogoFarmacia
from .forms import CatalogoFarmaciaForm

class CatalogoFarmaciaListView(ListView):
    model = CatalogoFarmacia
    template_name = 'farmacia/catalogo_list.html'
    context_object_name = 'productos'

class CatalogoFarmaciaCreateView(CreateView):
    model = CatalogoFarmacia
    form_class = CatalogoFarmaciaForm
    template_name = 'farmacia/catalogo_form.html'
    success_url = reverse_lazy('catalogo_list')

    def form_valid(self, form):
        messages.success(self.request, "Producto creado exitosamente.")
        return super().form_valid(form)

class CatalogoFarmaciaUpdateView(UpdateView):
    model = CatalogoFarmacia
    form_class = CatalogoFarmaciaForm
    template_name = 'farmacia/catalogo_form.html'
    success_url = reverse_lazy('catalogo_list')

    def form_valid(self, form):
        messages.success(self.request, "Producto actualizado correctamente.")
        return super().form_valid(form)

class CatalogoFarmaciaDeleteView(DeleteView):
    model = CatalogoFarmacia
    template_name = 'farmacia/catalogo_confirm_delete.html'
    success_url = reverse_lazy('catalogo_list')

    def form_valid(self, form):
        messages.success(self.request, "Producto eliminado correctamente.")
        return super().form_valid(form)
