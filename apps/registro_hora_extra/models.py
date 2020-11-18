from django.db import models
from apps.funcionarios.models import Funcionario


class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100, verbose_name='Motivo')
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    hora_extra = models.DecimalField(max_digits=5, decimal_places=2,
                                     verbose_name='Hora Extra', default=0);

    def __str__(self):
        return self.motivo

