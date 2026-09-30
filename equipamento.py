
from database.bd_equipamento import db_equipamento_cria
from database.bd_equipamento import db_equipamento_lista

from menus.cabecalho import cabecalho
from menus.exibir_menu_equipamento import exibir_menu_equipamentos

from utils.gerar_id import gerar_id_equipamento
from utils.validar_criticidade import validar_criticidade
from utils.validar_status import validar_status
from utils.exibir_lista import exibir_lista

def cadastrar_equipamento():
  equipamento = {
    "id" : gerar_id_equipamento(db_equipamento_lista()),
    "nome" : input("Nome do equipamento: "),
    "fabricante" : input("Fabricante: "),
    "modelo" : input("Modelo: "),
    "numero_de_serie" : input("Número de Série: "),
    "setor" : input("Setor: "),
    "data_aquisicao" : input("Data de aquisição: "),
    
    "criticidade" : validar_criticidade(),
    "status" : validar_status()
  }
  
  db_equipamento_cria(equipamento)

def lista_de_equipamento(lista_equipamento):
  cabecalho("Lista de Equipamentos")
  for equipamento in lista_equipamento:
    print("-" * 80)
    for chave, valor in equipamento.items():
      exibir_lista(chave, valor)

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
      print("Voltando ao menu principal")
      break
    
    #Entra em Equipamentos#
    elif (opcao == 1):
      cadastrar_equipamento()

    elif (opcao == 2):
      lista_de_equipamento(db_equipamento_lista())
    
    else:
      print("Opção Invalida. Digite alguma das opções")
      input("Pressione ENTER para continuar...")