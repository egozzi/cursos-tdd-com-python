from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao
from src.leilao.excecoes import LanceInvalido


class TestLeilao(TestCase):

    def setUp(self):
        self.gui = Usuario('Gui', 500.0)
        self.yuri = Usuario('Yuri', 500.0)
        self.vini = Usuario('Vini', 500.0)

        self.menor_valor_esperado = 100.0
        self.maior_valor_esperado = 150.0

        self.lance_do_yuri = Lance(self.yuri, self.menor_valor_esperado)
        self.lance_do_gui = Lance(self.gui, self.maior_valor_esperado)
        self.lance_do_vini = Lance(self.vini, self.menor_valor_esperado+1.0)

        self.leilao = Leilao('Celular')

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        self.leilao.propoe(self.lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)

        self.assertEqual(self.menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(self.maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(self.lance_do_yuri)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_do_yuri)

        self.assertEqual(self.menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(self.menor_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        self.leilao.propoe(self.lance_do_yuri)
        self.leilao.propoe(self.lance_do_vini)
        self.leilao.propoe(self.lance_do_gui)

        self.assertEqual(self.menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(self.maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_permitir_propor_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_do_gui)

        quantidade_de_lance_recebido = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lance_recebido)

    def test_deve_permitir_propor_lance_caso_o_ultimo_usuario_seja_diferente(self):
        self.leilao.propoe(self.lance_do_vini)
        self.leilao.propoe(self.lance_do_gui)

        quantidade_de_lance_recebido = len(self.leilao.lances)
        self.assertEqual(2, quantidade_de_lance_recebido)

    # se o último usuário for o mesmo, não deve permitir propor um lance
    def test_nao_deve_permitir_propor_lance_caso_o_ultimo_usuario_seja_igual(self):
        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(self.lance_do_gui)
