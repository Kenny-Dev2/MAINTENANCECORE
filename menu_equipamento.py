
from database.bd_equipamento import db_equipamento_cria
from database.bd_equipamento import db_equipamento_lista

from menus.cabecalho import cabecalho
from menus.exibir_menu_equipamento import exibir_menu_equipamentos

from utils.gerar_id import gerar_id
from utils.validar_codigo import validar_codigo
from utils.equipamento.validar_numero_serie_equipamento import validar_numero_serie_equipamento
from utils.equipamento.validar_setor import validar_setor
from utils.equipamento.validar_criticidade import validar_criticidade
from utils.equipamento.validar_status import validar_status
from utils.exibir_lista import exibir_lista
from utils.limpar_tela import limpar_tela

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

def lista_de_equipamento(lista_equipamento):
  cabecalho("Lista de Equipamentos")
  for equipamento in lista_equipamento:
    print("-" * 80)
    for chave, valor in equipamento.items():
      exibir_lista(chave, valor)

def consultar_equipamento():
  print("Consulta feita")

def menu_equipamento():
  while True:

    exibir_menu_equipamentos()

    try:
      opcao = int(input("Escolha uma opção: "))
    except ValueError:
      print("Opcao Invalida.")
      input("Pressione ENTER para continuar...")
      continue
    
    #Sai do programa#
    if(opcao == 7):
      limpar_tela()
      print("Voltando ao menu principal")
      break
    
    #Entra em Equipamentos#
    elif (opcao == 1):
      cadastrar_equipamento()

    elif (opcao == 2):
      lista_de_equipamento(db_equipamento_lista())

    elif (opcao == 3):
      consultar_equipamento()
    
    else:
      print("Opção Invalida. Digite alguma das opções")
      input("Pressione ENTER para continuar...")