# -*- coding: utf-8 -*-

from django.db import models


class Advogado(models.Model):
    nome = models.CharField(max_length=60, name='Nome'),
    telefone = models.CharField(max_length=11, name='Telefone'),
    email = models.CharField(max_length=60, name='E-mail'),
    cpf = models.CharField(max_length=11, name='CPF'),
