def validar_numero_serie_equipamento(lista_banco):

  while True:

    serie = input("Digite o numero de serie: ")
    serie_existe = False

    for item_lista in lista_banco:
      if (item_lista["numero_de_serie"] == serie):
        serie_existe = True
        break

    if serie_existe:
      print("Numero de serie já cadastrado")
    else:
      return serie