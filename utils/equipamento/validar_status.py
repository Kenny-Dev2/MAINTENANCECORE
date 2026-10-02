def validar_status():
  print("""
Status:
1 - Operacional
2 - Em Manutenção
3 - Parado
4 - Desativado
  """)

  while True:
    try:
      status = int(input("Escolha o status: "))
    except ValueError:
      print("Opcao Invalida.")
      input("Pressione ENTER para continuar...")
      continue

    if (status == 1):
      return "operacional"
    elif (status == 2):
      return "em manutenção"
    elif (status == 3):
      return "parado"
    elif (status == 4):
      return "desativado"
    else:
      print("Opção invalida\n")