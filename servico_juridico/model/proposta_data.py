# -*- coding: utf-8 -*-

from django.db import models
from servico_juridico.model.advogado_data import Advogado
from servico_juridico.model.ordem_servico_data import OrdemServico


class Proposta(models.Model):
    advogado_id = models.ForeignKey(Advogado, name='Advogado'),
    ordem_servico_id = models.ForeignKey(OrdemServico, name='Ordem de Servico'),
    valor_execucao = models.FloatField(name='Valor para execucao'),
    proposta_aceita = models.BooleanField(name='Proposta aceita'),
