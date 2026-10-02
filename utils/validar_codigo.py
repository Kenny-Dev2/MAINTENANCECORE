def validar_codigo(lista_banco, prefixo, setor):

  while True:

    codigo = prefixo + input("Digite o codigo " + setor + ": ")
    codigo_existe = False

    for item_lista in lista_banco:
      if (item_lista["codigo"] == codigo):
        codigo_existe = True
        break

    if codigo_existe:
      print("Codigo já cadastrado")
    else:
      return codigo