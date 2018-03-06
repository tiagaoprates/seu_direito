# -*- coding: utf-8 -*-

from servico_juridico.model.ordem_servico_data import OrdemServico


class OrdemServicoControl(OrdemServico):
    class Meta:
        proxy = True
        permissions = (
            ("add_ordem_servico", "Criar uma ordem de servico"),
            ("change_ordem_servico", "Alterar uma ordem de servico"),
            ("delete_ordem_servico", "Deletar uma ordem de servico"),
        )

    def finaliza_ordem_servico(self):
        self.state = self.FINALIZADA
        self.save()
        return self.state

