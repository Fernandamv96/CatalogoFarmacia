from django import forms
from django.utils import timezone

from .models import CatalogoFarmacia


class CatalogoFarmaciaForm(forms.ModelForm):
    class Meta:
        model = CatalogoFarmacia
        fields = ["nombre", "descripcion", "precio", "stock", "fecha_vencimiento"]
        widgets = {
            "fecha_vencimiento": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "precio": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "stock": forms.NumberInput(attrs={"class": "form-control"}),
        }

    def clean_fecha_vencimiento(self):
        fecha = self.cleaned_data.get("fecha_vencimiento")
        if fecha and fecha < timezone.now().date():
            raise forms.ValidationError(
                "La fecha de vencimiento no puede ser anterior al día de hoy."
            )
        return fecha
