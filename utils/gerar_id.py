def gerar_id(lista_equipamentos):
  if not lista_equipamentos:
    return 1
  return lista_equipamentos[-1]["id"] + 1