from django.test import TestCase
from servico_juridico.model.empresa_data import Empresa
from servico_juridico.model.ordem_servico_data import OrdemServico


class PropostaTestCase(TestCase):
    def setUp(self):
        Empresa.objects.create(nome='Produtos Alimenticios LTDA', ramo_atuacao='Alimentos')
        OrdemServico.objects.create(empresa_id=Empresa.id, titulo='ABC',
                                    descricao='Teste teste teste')

    def test_ordem_servico_state(self):
        nova_ordem = OrdemServico.objects.get(titulo='ABC')
        self.assertEqual(nova_ordem.finaliza_ordem_servico(), nova_ordem.FINALIZADA)
