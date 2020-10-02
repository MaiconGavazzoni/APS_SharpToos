from django.db import models
from django.conf import settings

class Tools(models.Model):
    stock_code = models.IntegerField('Código', blank=False)
    internal_description = models.CharField('Descrição', max_length=150, blank=False)
    factory_name = models.CharField('Nome de Fábrica', max_length=150, blank=False)
    manufacturer = models.CharField('Fabricante', max_length=100, blank=False)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)
    def __str__(self):
        return self.internal_description

    class Meta:
        verbose_name = 'Ferramenta'
        verbose_name_plural = 'Ferramentas'
        ordering = ['stock_code']

class Sharpen(models.Model):
    name_sharpen = models.CharField('Lista', max_length=100)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='Autor', related_name='nome', on_delete=models.CASCADE
    )
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.name_sharpen

    class Meta:
        verbose_name = 'Lista'
        verbose_name_plural = 'Listas'
        ordering = ['-created']

class ListSharpen(models.Model):
    tools = models.ForeignKey(Tools,
        verbose_name='Ferramenta', related_name='description', blank=False,
        on_delete=models.CASCADE
    )
    sharpen = models.ForeignKey(Sharpen, related_name='Lista',blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField('Quantidade', blank=False)



