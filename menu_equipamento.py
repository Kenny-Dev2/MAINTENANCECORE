from equipamento.cadastrar import cadastrar_equipamento
from equipamento.listar import lista_de_equipamento

from menus.exibir_menu_equipamento import exibir_menu_equipamentos

from utils.exibir_lista import exibir_lista
from utils.limpar_tela import limpar_tela

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
      lista_de_equipamento()

    elif (opcao == 3):
      print("Consultar banco")
    
    else:
      print("Opção Invalida. Digite alguma das opções")
      input("Pressione ENTER para continuar...")