from servico_juridico.model.proposta_data import Proposta


class PropostaControl(Proposta):
    class Meta:
        proxy = True
        permissions = (
            ("add_proposta", "Criar uma proposta"),
            ("change_proposta", "ALterar uma proposta"),
            ("delete_proposta", "Deletar uma proposta"),
        )

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        res = super(Proposta, self).save(force_insert, force_update, using, update_fields)
        if self.proposta_aceita:
            self.ordem_servico_id.state = self.ordem_servico_id.DELEGADA
        else:
            self.ordem_servico_id.state = self.ordem_servico_id.CRIADA
        self.ordem_servico_id.save()
        return res
