def validar_setor(criticidade):
  while True:
    setor = input("Setor: ")

    if criticidade == "crítico" and not setor:
      print("Equipamento crítico precisa ter um setor.")
      continue

    return setor