# -*- coding: utf-8 -*-

from django.db import models
from servico_juridico.model.empresa_data import Empresa


class OrdemServico(models.Model):
    CRIADA = 'C'
    DELEGADA = 'D'
    FINALIZADA = 'F'
    STATUS_ORDEM_SERVICO = ((CRIADA, 'Criada'), (DELEGADA, 'Delegada'), (FINALIZADA, 'Finalizada'))

    empresa_id = models.ForeignKey(Empresa, name='Empresa'),
    titulo = models.CharField(max_length=60, name='Titulo'),
    descricao = models.TextField(name='Descricao'),
    state = models.CharField(max_length=1, choices=STATUS_ORDEM_SERVICO, name='Status',
                             default=CRIADA),
