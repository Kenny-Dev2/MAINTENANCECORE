from database.bd_equipamento import db_equipamento_cria
from database.bd_equipamento import db_equipamento_lista

from menus.cabecalho import cabecalho
from menus.exibir_menu_equipamento import exibir_menu_equipamentos

from utils.gerar_id import gerar_id
from utils.validar_codigo import validar_codigo
from utils.exibir_lista import exibir_lista
from utils.limpar_tela import limpar_tela

from equipamento.utils.validar_criticidade import validar_criticidade
from equipamento.utils.validar_numero_serie_equipamento import validar_numero_serie_equipamento
from equipamento.utils.validar_setor import validar_setor
from equipamento.utils.validar_status import validar_status

def cadastrar_equipamento():

  criticidade = validar_criticidade()

  equipamento = {
    "id" : gerar_id(db_equipamento_lista()),
    "codigo": validar_codigo(db_equipamento_lista(), "EQP-", "do equipamento"),
    "nome" : input("Nome do equipamento: "),
    "fabricante" : input("Fabricante: "),
    "modelo" : input("Modelo: "),
    "numero_de_serie" : validar_numero_serie_equipamento(db_equipamento_lista()),
    "setor" : validar_setor(criticidade),
    "data_aquisicao" : input("Data de aquisição: "),
    
    "criticidade" : criticidade,
    "status" : validar_status()
  }

  if(equipamento["criticidade"] == "crítico" and not equipamento["setor"]):
    return "Equipamento critico, necessita está vinculado a um setor"
  
  db_equipamento_cria(equipamento)