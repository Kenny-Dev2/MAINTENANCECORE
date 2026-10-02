def validar_criticidade():
  print("""
Criticidade:
1 - Baixa
2 - Média
3 - Alta
4 - Crítica
  """)

  while True:
    try:
      criticidade = int(input("Escolha a criticidade: "))
    except ValueError:
      print("Opcao Invalida.")
      input("Pressione ENTER para continuar...")
      continue

    if (criticidade == 1):
      return "baixa"
    elif (criticidade == 2):
      return "média"
    elif (criticidade == 3):
      return "alta"
    elif (criticidade == 4):
      return "crítico"
    else:
      print("Opção invalida\n")