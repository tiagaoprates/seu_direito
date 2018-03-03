# -*- coding: utf-8 -*-

from django.db import models


class Empresa(models.Model):
    nome = models.CharField(max_length=60, name='Nome'),
    ramo_atuacao = models.CharField(max_length=30, name='Ramo de atuacao'),
