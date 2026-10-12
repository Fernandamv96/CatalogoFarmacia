from datetime import date, timedelta

from django.test import TestCase
from django.urls import reverse

from .models import CatalogoFarmacia


class CatalogoFarmaciaTests(TestCase):
    def setUp(self):
        self.producto = CatalogoFarmacia.objects.create(
            nombre='Paracetamol', precio='2.50', stock=10,
            fecha_vencimiento=date.today() + timedelta(days=30),
        )

    def test_listado(self):
        respuesta = self.client.get(reverse('catalogo_list'))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, 'Paracetamol')

    def test_crear(self):
        respuesta = self.client.post(reverse('catalogo_create'), {
            'nombre': 'Ibuprofeno', 'precio': '3.00', 'stock': 5,
            'fecha_vencimiento': date.today() + timedelta(days=60),
        })
        self.assertRedirects(respuesta, reverse('catalogo_list'))
        self.assertTrue(CatalogoFarmacia.objects.filter(nombre='Ibuprofeno').exists())

    def test_no_permite_fecha_vencida(self):
        respuesta = self.client.post(reverse('catalogo_create'), {
            'nombre': 'Vencido', 'precio': '1.00', 'stock': 1,
            'fecha_vencimiento': date.today() - timedelta(days=1),
        })
        self.assertEqual(respuesta.status_code, 200)
        self.assertFalse(CatalogoFarmacia.objects.filter(nombre='Vencido').exists())

    def test_eliminar(self):
        respuesta = self.client.post(reverse('catalogo_delete', args=[self.producto.pk]))
        self.assertRedirects(respuesta, reverse('catalogo_list'))
        self.assertFalse(CatalogoFarmacia.objects.exists())
