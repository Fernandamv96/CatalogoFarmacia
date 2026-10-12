from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone


class CatalogoFarmacia(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Producto")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    precio = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)], verbose_name="Precio"
    )
    stock = models.PositiveIntegerField(default=0, verbose_name="Stock disponible")
    fecha_vencimiento = models.DateField(verbose_name="Fecha de Vencimiento")

    class Meta:
        verbose_name = "Producto de Farmacia"
        verbose_name_plural = "Catálogo de Farmacia"
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

    @property
    def esta_vencido(self):
        return self.fecha_vencimiento < timezone.now().date()

    @property
    def dias_para_vencer(self):
        return (self.fecha_vencimiento - timezone.now().date()).days

    @property
    def estado(self):
        """'vencido', 'por_vencer' (30 días o menos) o 'vigente'."""
        if self.esta_vencido:
            return "vencido"
        if self.dias_para_vencer <= 30:
            return "por_vencer"
        return "vigente"

    @property
    def stock_bajo(self):
        return self.stock <= 5
