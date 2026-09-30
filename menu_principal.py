from menus.exibir_menu_principal import exibir_menu_principal
import equipamento

def menu_principal():
  while True:
    
    exibir_menu_principal();
    
    try:
      opcao = int(input("Escolha uma opção: "))
    except ValueError:
      print("Opcao Invalida.")
      input("Pressione ENTER para continuar...")
      continue

    #Sai do programa#
    if(opcao == 0):
      print("Saindo do programa...")
      break

    #Entra em Equipamentos#
    elif (opcao == 1):
      equipamento.menu_equipamento()

    else:
      print("Opção Invalida. Digite alguma das opções")
      input("Pressione ENTER para continuar...")